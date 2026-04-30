"""
Demonstrates how to create and work with arrays (lists) of network subnets.

Practical use cases include:
- Allocating subnets per department or office location
- Subdividing a large address block for cloud infrastructure
- Building VLAN subnet pools for network segmentation
- Generating sequential subnets for automated provisioning

All top-level variables can be modified to match your organization's
addressing scheme and business requirements.
"""

import ipaddress
from typing import List, Dict, Optional, Union

# ---------------------------------------------------------------------------
# User-configurable variables — adjust these to fit your environment
# ---------------------------------------------------------------------------

# Parent network to subdivide (CIDR notation)
PARENT_NETWORK: str = "10.0.0.0/8"

# Prefix length for each child subnet carved from PARENT_NETWORK
SUBNET_PREFIX: int = 24  # /24 → 254 usable hosts per subnet

# A fixed list of subnets already allocated across the organization
ALLOCATED_SUBNETS: List[str] = [
    "10.1.0.0/24",   # HQ — floor 1
    "10.1.1.0/24",   # HQ — floor 2
    "10.2.0.0/24",   # Branch office — Dallas
    "10.3.0.0/24",   # Branch office — Chicago
    "10.4.0.0/16",   # Data center — primary
    "10.5.0.0/16",   # Data center — DR
]

# Department names mapped to how many /24 subnets they need
DEPARTMENT_REQUIREMENTS: Dict[str, int] = {
    "Engineering":  4,
    "Finance":      2,
    "HR":           1,
    "Marketing":    2,
    "Operations":   3,
}

# Starting address block used when assigning subnets to departments
DEPARTMENT_BASE_NETWORK: str = "172.16.0.0/12"
DEPARTMENT_SUBNET_PREFIX: int = 24

# Named environments and the address block reserved for each
ENVIRONMENT_BLOCKS: Dict[str, str] = {
    "production":  "192.168.0.0/18",
    "staging":     "192.168.64.0/18",
    "development": "192.168.128.0/18",
    "testing":     "192.168.192.0/18",
}
# Prefix length for slices carved from each environment block
ENVIRONMENT_SUBNET_PREFIX: int = 24

# Maximum number of subnets to generate in a single call (safety limit)
MAX_SUBNETS: int = 256


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def create_subnet_array(
    parent_cidr: str,
    new_prefix: int,
    limit: Optional[int] = None,
) -> List[str]:
    """
    Subdivide a parent network into an array of equal-sized subnets.

    Args:
        parent_cidr: Parent network in CIDR notation (e.g. '10.0.0.0/8').
        new_prefix:  Prefix length for each child subnet (must be > parent prefix).
        limit:       Maximum number of subnets to return.  Defaults to MAX_SUBNETS.

    Returns:
        List of subnet strings in CIDR notation, ordered numerically.

    Example:
        >>> create_subnet_array("10.0.0.0/22", 24)
        ['10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']
    """
    cap = limit if limit is not None else MAX_SUBNETS
    parent = ipaddress.ip_network(parent_cidr, strict=False)

    if new_prefix <= parent.prefixlen:
        raise ValueError(
            f"new_prefix ({new_prefix}) must be larger than "
            f"parent prefix ({parent.prefixlen})."
        )

    subnets: List[str] = []
    for subnet in parent.subnets(new_prefix=new_prefix):
        if len(subnets) >= cap:
            break
        subnets.append(str(subnet))

    return subnets


def assign_subnets_to_departments(
    base_cidr: str,
    subnet_prefix: int,
    requirements: Dict[str, int],
) -> Dict[str, List[str]]:
    """
    Sequentially allocate subnet blocks to named departments.

    Subnets are drawn in order from *base_cidr*; each department receives
    exactly as many consecutive subnets as specified in *requirements*.

    Args:
        base_cidr:      Starting address block in CIDR notation.
        subnet_prefix:  Prefix length for each allocated subnet.
        requirements:   Mapping of department name → number of subnets needed.

    Returns:
        Dictionary of department name → list of assigned subnet strings.

    Example:
        >>> assign_subnets_to_departments(
        ...     "172.16.0.0/12", 24, {"Eng": 2, "HR": 1}
        ... )
        {'Eng': ['172.16.0.0/24', '172.16.1.0/24'], 'HR': ['172.16.2.0/24']}
    """
    # Pre-generate the full pool of available subnets from the base block
    pool = create_subnet_array(base_cidr, subnet_prefix)
    pool_iter = iter(pool)

    allocation: Dict[str, List[str]] = {}
    for department, count in requirements.items():
        assigned: List[str] = []
        for _ in range(count):
            try:
                assigned.append(next(pool_iter))
            except StopIteration:
                raise RuntimeError(
                    "Address pool exhausted before all departments were allocated."
                )
        allocation[department] = assigned

    return allocation


def build_environment_subnet_map(
    env_blocks: Dict[str, str],
    subnet_prefix: int,
    limit: Optional[int] = None,
) -> Dict[str, List[str]]:
    """
    Create a subnet array for each named environment from its reserved block.

    Args:
        env_blocks:    Mapping of environment name → parent CIDR block.
        subnet_prefix: Prefix length for individual subnets within each block.
        limit:         Maximum subnets to include per environment.

    Returns:
        Dictionary of environment name → list of subnet strings.

    Example:
        >>> build_environment_subnet_map(
        ...     {"prod": "10.10.0.0/22"}, 24, limit=2
        ... )
        {'prod': ['10.10.0.0/24', '10.10.1.0/24']}
    """
    return {
        env: create_subnet_array(block, subnet_prefix, limit=limit)
        for env, block in env_blocks.items()
    }


def filter_available_subnets(
    pool: List[str],
    allocated: List[str],
) -> List[str]:
    """
    Return subnets from *pool* that do not overlap with any *allocated* subnet.

    Args:
        pool:      Full list of candidate subnets.
        allocated: List of already-allocated subnets to exclude.

    Returns:
        List of non-overlapping available subnets.

    Example:
        >>> filter_available_subnets(
        ...     ["10.0.0.0/24", "10.0.1.0/24"],
        ...     ["10.0.0.0/24"],
        ... )
        ['10.0.1.0/24']
    """
    allocated_networks: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]] = [
        ipaddress.ip_network(s, strict=False) for s in allocated
    ]

    available: List[str] = []
    for candidate_str in pool:
        candidate = ipaddress.ip_network(candidate_str, strict=False)
        # Keep the candidate only if it has no overlap with any allocated subnet
        if not any(candidate.overlaps(alloc) for alloc in allocated_networks):
            available.append(candidate_str)

    return available


def subnet_summary(subnets: List[str]) -> List[Dict[str, object]]:
    """
    Build a summary record for each subnet in the array.

    Useful for populating an IPAM spreadsheet or a configuration database.

    Args:
        subnets: List of subnet strings in CIDR notation.

    Returns:
        List of dictionaries, one per subnet, containing:
        - cidr              : subnet in CIDR notation
        - network_address   : first address in the block
        - broadcast_address : last address in the block
        - usable_hosts      : number of assignable host addresses
        - prefix_length     : numeric prefix (e.g. 24)

    Example:
        >>> subnet_summary(["10.0.0.0/30"])
        [{'cidr': '10.0.0.0/30', 'network_address': '10.0.0.0',
          'broadcast_address': '10.0.0.3', 'usable_hosts': 2, 'prefix_length': 30}]
    """
    records: List[Dict[str, object]] = []
    for cidr in subnets:
        net = ipaddress.ip_network(cidr, strict=False)
        # /32 (host route) has a single address; /31 (RFC 3021 point-to-point)
        # uses both addresses, so neither needs the -2 broadcast/network adjustment
        if net.prefixlen >= 31:
            usable = net.num_addresses
        else:
            usable = net.num_addresses - 2  # subtract network & broadcast

        records.append(
            {
                "cidr": str(net),
                "network_address": str(net.network_address),
                "broadcast_address": str(net.broadcast_address),
                "usable_hosts": usable,
                "prefix_length": net.prefixlen,
            }
        )
    return records


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # --- 1. Carve /24s from the corporate address space ---
    print("=== Subnets carved from parent network ===")
    carved = create_subnet_array(PARENT_NETWORK, SUBNET_PREFIX, limit=6)
    for s in carved:
        print(f"  {s}")

    # --- 2. Assign subnet blocks to each department ---
    print("\n=== Department subnet allocations ===")
    dept_map = assign_subnets_to_departments(
        DEPARTMENT_BASE_NETWORK,
        DEPARTMENT_SUBNET_PREFIX,
        DEPARTMENT_REQUIREMENTS,
    )
    for dept, subnets in dept_map.items():
        print(f"  {dept}: {subnets}")

    # --- 3. Build per-environment subnet arrays ---
    print("\n=== Environment subnet pools (first 3 per environment) ===")
    env_map = build_environment_subnet_map(
        ENVIRONMENT_BLOCKS,
        ENVIRONMENT_SUBNET_PREFIX,
        limit=3,  # show only 3 per environment for readability
    )
    for env, subnets in env_map.items():
        print(f"  {env}: {subnets}")

    # --- 4. Find subnets still available for new allocations ---
    print("\n=== Available subnets (not yet allocated) ===")
    full_pool = create_subnet_array("10.0.0.0/21", 24)  # 8 × /24s
    available = filter_available_subnets(full_pool, ALLOCATED_SUBNETS)
    print(f"  Pool size    : {len(full_pool)}")
    print(f"  Available    : {len(available)}")
    for s in available:
        print(f"    {s}")

    # --- 5. Print a summary table for a small block ---
    print("\n=== Subnet summary for 10.10.0.0/22 → /24s ===")
    summary_subnets = create_subnet_array("10.10.0.0/22", 24)
    for record in subnet_summary(summary_subnets):
        print(
            f"  {record['cidr']:<20}"
            f"  hosts={record['usable_hosts']:<5}"
            f"  network={record['network_address']}"
        )
