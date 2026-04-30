"""network_subnets.py

Functions for IPv4 subnet calculations:
  - Determining network address, usable host range, and broadcast address
  - Dividing a network into n equal-capacity subnets
  - Dividing a network into subnets with specific host capacities (VLSM)
  - Rendering results as a PrettyTable
"""

import math
import ipaddress
from prettytable import PrettyTable


def get_subnet_details(network: ipaddress.IPv4Network) -> dict:
    """Return key addressing details for a single IPv4 network.

    Args:
        network: An IPv4Network object to inspect.

    Returns:
        Dict with keys: network, subnet_mask, prefix_length, network_address,
        first_usable, last_usable, usable_hosts, broadcast_address.
    """
    hosts = list(network.hosts())
    return {
        "network": str(network),
        "subnet_mask": str(network.netmask),
        "prefix_length": network.prefixlen,
        "network_address": str(network.network_address),
        "first_usable": str(hosts[0]) if hosts else "N/A",
        "last_usable": str(hosts[-1]) if hosts else "N/A",
        "usable_hosts": len(hosts),
        "broadcast_address": str(network.broadcast_address),
    }


def equal_capacity_subnets(
    base_network: str, n: int, verbose: bool = True
) -> list[dict]:
    """Divide *base_network* into *n* equal-capacity subnets.

    Steps performed:
      1. Parse and validate the base network CIDR string.
      2. Calculate the minimum prefix-length increment needed to produce >= n subnets.
      3. Generate all resulting equal-sized subnets.
      4. Collect and return details for each subnet.

    Args:
        base_network: CIDR notation string, e.g. "192.168.1.0/24".
        n: Number of equal subnets desired.
        verbose: When True, print step-by-step progress to stdout.

    Returns:
        List of subnet-detail dicts (one per subnet) from get_subnet_details().

    Raises:
        ValueError: If splitting would require a prefix longer than /32.
    """
    steps = []

    steps.append(f"Step 1: Parse base network '{base_network}'.")
    network = ipaddress.ip_network(base_network, strict=False)
    steps.append(f"        Validated: {network}  (prefix /{network.prefixlen})")

    steps.append(
        f"Step 2: Calculate prefix-length increment to produce >= {n} subnets."
    )
    prefixlen_diff = math.ceil(math.log2(n)) if n > 1 else 0
    new_prefix = network.prefixlen + prefixlen_diff
    actual_count = 2**prefixlen_diff
    steps.append(
        f"        Increment: +{prefixlen_diff}  →  new prefix /{new_prefix}  "
        f"→  yields {actual_count} subnets (need {n})."
    )

    if new_prefix > 32:
        raise ValueError(
            f"Cannot split {network} into {n} equal subnets; "
            f"required prefix /{new_prefix} exceeds /32."
        )

    steps.append(f"Step 3: Generate all /{new_prefix} subnets from {network}.")
    subnets = list(network.subnets(prefixlen_diff=prefixlen_diff))
    steps.append(f"        Generated {len(subnets)} subnet(s).")

    steps.append("Step 4: Collect addressing details for each subnet.")
    results = [get_subnet_details(s) for s in subnets]

    if verbose:
        print("\n--- Equal-Capacity Subnet Allocation ---")
        for step in steps:
            print(step)

    return results


def specific_capacity_subnets(
    base_network: str, capacities: list[int], verbose: bool = True
) -> list[dict]:
    """Allocate subnets from *base_network* sized to specific host requirements (VLSM).

    Variable Length Subnet Masking (VLSM) assigns the smallest valid subnet to
    each requirement, conserving address space for remaining allocations.

    Steps performed:
      1. Parse and validate the base network CIDR string.
      2. Sort capacity requirements descending (largest requirement first).
      3. For each requirement, determine the smallest subnet prefix that fits.
      4. Select the best-fit available block and carve the subnet from it.
      5. Collect and return details for each allocated subnet.

    Args:
        base_network: CIDR notation string, e.g. "10.0.0.0/24".
        capacities: Required usable host counts per subnet, e.g. [50, 20, 10].
        verbose: When True, print step-by-step progress to stdout.

    Returns:
        List of subnet-detail dicts in allocation order (largest first).
        Each dict includes a 'requested_hosts' key with the original requirement.

    Raises:
        ValueError: If any requirement cannot be satisfied by the remaining space.
    """
    steps = []

    steps.append(f"Step 1: Parse base network '{base_network}'.")
    network = ipaddress.ip_network(base_network, strict=False)
    steps.append(f"        Validated: {network}  (/{network.prefixlen})")

    steps.append(
        f"Step 2: Sort {len(capacities)} requirements descending "
        f"(largest host count first)."
    )
    indexed = sorted(enumerate(capacities), key=lambda x: x[1], reverse=True)
    steps.append(
        f"        Sorted: {[c for _, c in indexed]}  "
        f"(original positions: {[i for i, _ in indexed]})"
    )

    if any(c < 1 for _, c in indexed):
        raise ValueError("All capacity requirements must be at least 1 usable host.")

    steps.append("Steps 3-4: Allocate subnets using best-fit VLSM.")
    available: list[ipaddress.IPv4Network] = [network]
    allocated: list[tuple[int, dict]] = []

    for original_idx, capacity in indexed:
        needed_addresses = capacity + 2  # add network address and broadcast
        # Enforce minimum of 2 host bits (→ /30) so every subnet has a
        # distinct network address, usable range, and broadcast address.
        host_bits = max(2, math.ceil(math.log2(needed_addresses)))
        required_prefix = 32 - host_bits

        steps.append(
            f"        Requirement [{original_idx + 1}]: {capacity} hosts  "
            f"→  {needed_addresses} addresses needed  →  /{required_prefix}"
        )

        # Sort available blocks by size ascending (highest prefix first)
        # so we pick the smallest block that still fits the requirement.
        available.sort(key=lambda b: b.prefixlen, reverse=True)

        allocated_subnet = None
        for i, block in enumerate(available):
            if block.prefixlen <= required_prefix:
                candidate = next(block.subnets(new_prefix=required_prefix))
                allocated_subnet = candidate
                leftovers = list(block.address_exclude(candidate))
                available = available[:i] + leftovers + available[i + 1:]
                steps.append(
                    f"          → Allocated {candidate} from block {block}.  "
                    f"Remaining free blocks: {len(available)}"
                )
                break

        if allocated_subnet is None:
            raise ValueError(
                f"Insufficient address space for {capacity} hosts "
                f"(requirement #{original_idx + 1})."
            )

        detail = get_subnet_details(allocated_subnet)
        detail["requested_hosts"] = capacity
        allocated.append((original_idx, detail))

    steps.append("Step 5: Collect results (in allocation order, largest first).")
    results = [detail for _, detail in allocated]

    if verbose:
        print("\n--- VLSM Subnet Allocation ---")
        for step in steps:
            print(step)

    return results


def display_subnets(
    subnets: list[dict],
    title: str = "Subnet Details",
    include_requested: bool = False,
) -> PrettyTable:
    """Render subnet details as a formatted PrettyTable.

    Args:
        subnets: List of subnet-detail dicts from get_subnet_details() or
                 specific_capacity_subnets().
        title: Heading printed above and embedded in the table.
        include_requested: When True, adds a 'Requested' column showing the
                           'requested_hosts' value (used with VLSM output).

    Returns:
        The populated PrettyTable instance.
    """
    columns = [
        "Network",
        "Mask",
        "Network Address",
        "First Usable",
        "Last Usable",
        "Usable Hosts",
        "Broadcast",
    ]
    if include_requested:
        columns.insert(1, "Requested")

    table = PrettyTable(columns)
    table.title = title
    table.align = "l"

    for s in subnets:
        row = [
            s["network"],
            s["subnet_mask"],
            s["network_address"],
            s["first_usable"],
            s["last_usable"],
            s["usable_hosts"],
            s["broadcast_address"],
        ]
        if include_requested:
            row.insert(1, s.get("requested_hosts", "N/A"))
        table.add_row(row)

    print(f"\n{title}")
    print(table)
    return table


if __name__ == "__main__":
    # ------------------------------------------------------------------ #
    # Example 1 – Equal-capacity subnets                                  #
    # Split 192.168.10.0/24 into 4 equal subnets (/26 each, 62 hosts ea) #
    # ------------------------------------------------------------------ #
    print("=" * 70)
    print("EXAMPLE 1: Split 192.168.10.0/24 into 4 equal subnets")
    print("=" * 70)
    equal_nets = equal_capacity_subnets("192.168.10.0/24", 4)
    display_subnets(equal_nets, title="Equal-Capacity Subnets — 192.168.10.0/24 ÷ 4")

    # ------------------------------------------------------------------ #
    # Example 2 – VLSM subnets with specific capacities                  #
    # Carve four differently-sized subnets out of 10.0.0.0/24            #
    # ------------------------------------------------------------------ #
    print("\n" + "=" * 70)
    print("EXAMPLE 2: VLSM allocation from 10.0.0.0/24")
    print("  Requirements: 50 hosts, 25 hosts, 10 hosts, 5 hosts")
    print("=" * 70)
    vlsm_nets = specific_capacity_subnets("10.0.0.0/24", [50, 25, 10, 5])
    display_subnets(
        vlsm_nets,
        title="VLSM Subnets — 10.0.0.0/24",
        include_requested=True,
    )

    # ------------------------------------------------------------------ #
    # Example 3 – Six equal subnets from a /20 block                     #
    # ------------------------------------------------------------------ #
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Split 172.16.0.0/20 into 6 equal subnets")
    print("=" * 70)
    large_nets = equal_capacity_subnets("172.16.0.0/20", 6)
    display_subnets(large_nets, title="Equal-Capacity Subnets — 172.16.0.0/20 ÷ 6")
