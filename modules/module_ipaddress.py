import ipaddress
from typing import List, Tuple, Optional
import csv
from pathlib import Path

"""
The ipaddress module provides capabilities for creating, manipulating, and performing operations on IPv4 and IPv6 addresses and networks.
"""


def validate_ip_address(ip_str: str) -> Tuple[bool, Optional[str]]:
    """
    Use case: Data validation in ETL pipelines for network logs.

    Args:
        ip_str: String representation of an IP address

    Returns:
        Tuple of (is_valid, ip_type) where ip_type is 'IPv4', 'IPv6', or None
    """
    try:
        ip = ipaddress.ip_address(ip_str)
        return True, f"IPv{ip.version}"
    except ValueError:
        return False, None


def categorize_ip_addresses(ip_list: List[str]) -> dict:
    """
    Use case: Security analysis - identifying internal vs external traffic.

    Args:
        ip_list: List of IP address strings

    Returns:
        Dictionary with categorized IP addresses
    """
    categories = {
        "private": [],
        "public": [],
        "loopback": [],
        "multicast": [],
        "reserved": [],
        "invalid": [],
    }

    for ip_str in ip_list:
        try:
            ip = ipaddress.ip_address(ip_str)

            if ip.is_private:
                categories["private"].append(ip_str)
            elif ip.is_loopback:
                categories["loopback"].append(ip_str)
            elif ip.is_multicast:
                categories["multicast"].append(ip_str)
            elif ip.is_reserved:
                categories["reserved"].append(ip_str)
            else:
                categories["public"].append(ip_str)

        except ValueError:
            categories["invalid"].append(ip_str)

    return categories


def check_ip_in_subnet(ip_str: str, subnet_str: str) -> bool:
    """
    Use case: Network segmentation analysis, firewall rule validation.

    Args:
        ip_str: IP address string (e.g., '192.168.1.100')
        subnet_str: Subnet in CIDR notation (e.g., '192.168.1.0/24')

    Returns:
        True if IP is in subnet, False otherwise
    """
    try:
        ip = ipaddress.ip_address(ip_str)
        network = ipaddress.ip_network(subnet_str, strict=False)
        return ip in network
    except ValueError as e:
        print(f"Error: {e}")
        return False


def find_subnet_for_ips(ip_list: List[str], subnets: List[str]) -> dict:
    """
    Map each IP address to its corresponding subnet.

    Use case: Network topology mapping, cost allocation by network segment.

    Args:
        ip_list: List of IP addresses
        subnets: List of subnets in CIDR notation

    Returns:
        Dictionary mapping IP addresses to their subnets
    """
    ip_to_subnet = {}

    for ip_str in ip_list:
        try:
            ip = ipaddress.ip_address(ip_str)
            matched_subnet = None

            for subnet_str in subnets:
                network = ipaddress.ip_network(subnet_str, strict=False)
                if ip in network:
                    matched_subnet = subnet_str
                    break

            ip_to_subnet[ip_str] = matched_subnet

        except ValueError:
            ip_to_subnet[ip_str] = "INVALID"

    return ip_to_subnet


def calculate_subnet_info(cidr: str) -> dict:
    """
    Calculate detailed information about a subnet.

    Use case: Capacity planning, IP address management (IPAM).

    Args:
        cidr: Subnet in CIDR notation (e.g., '10.0.0.0/24')

    Returns:
        Dictionary with subnet details
    """
    try:
        network = ipaddress.ip_network(cidr, strict=False)

        return {
            "network_address": str(network.network_address),
            "broadcast_address": str(network.broadcast_address),
            "netmask": str(network.netmask),
            "prefix_length": network.prefixlen,
            "total_addresses": network.num_addresses,
            "usable_addresses": network.num_addresses - 2
            if network.version == 4 and network.prefixlen < 31
            else network.num_addresses,
            "first_usable": str(list(network.hosts())[0])
            if network.num_addresses > 2
            else "N/A",
            "last_usable": str(list(network.hosts())[-1])
            if network.num_addresses > 2
            else "N/A",
            "version": f"IPv{network.version}",
        }
    except (ValueError, IndexError) as e:
        return {"error": str(e)}


def generate_ip_range(start_ip: str, end_ip: str) -> List[str]:
    """
    Generate all IP addresses in a range.

    Use case: Creating IP allowlists, generating test data.

    Args:
        start_ip: Starting IP address
        end_ip: Ending IP address

    Returns:
        List of IP addresses in the range
    """
    try:
        start = ipaddress.ip_address(start_ip)
        end = ipaddress.ip_address(end_ip)

        # Ensure same IP version
        if start.version != end.version:
            raise ValueError("Start and end IP must be same version")

        ip_list = []
        current = int(start)
        end_int = int(end)

        # Limit to prevent memory issues
        if end_int - current > 10000:
            raise ValueError("Range too large (max 10000 addresses)")

        while current <= end_int:
            ip_list.append(str(ipaddress.ip_address(current)))
            current += 1

        return ip_list

    except ValueError as e:
        print(f"Error: {e}")
        return []


def find_supernet(subnets: List[str]) -> Optional[str]:
    """
    Find the smallest supernet that contains all given subnets.

    Use case: Network consolidation, route summarization.

    Args:
        subnets: List of subnet CIDR notations

    Returns:
        Supernet in CIDR notation or None if subnets are incompatible
    """
    try:
        networks = [ipaddress.ip_network(subnet, strict=False) for subnet in subnets]

        # Separate IPv4 and IPv6 networks
        ipv4_networks = [n for n in networks if n.version == 4]
        ipv6_networks = [n for n in networks if n.version == 6]

        # Can't create supernet from mixed IP versions
        if ipv4_networks and ipv6_networks:
            return None

        # Use supernet() method to find common supernet
        active_networks = ipv4_networks if ipv4_networks else ipv6_networks
        # Type checker needs explicit typing since collapse_addresses requires homogeneous network types
        from typing import cast, Union

        supernet = ipaddress.collapse_addresses(
            cast(Union[list, tuple], active_networks)
        )
        supernet_list = list(supernet)

        if len(supernet_list) == 1:
            return str(supernet_list[0])
        else:
            # Find minimum supernet that contains all
            all_ips = set()
            for net in active_networks:
                all_ips.update([net.network_address, net.broadcast_address])

            min_ip = min(all_ips)

            # Calculate required prefix length
            max_prefix = 33 if active_networks[0].version == 4 else 129
            for prefix in range(0, max_prefix):
                test_net = ipaddress.ip_network(f"{min_ip}/{prefix}", strict=False)
                # Ensure type compatibility by checking version
                if test_net.version == active_networks[0].version:
                    # Type narrowing: filter networks to ensure they match test_net's version
                    matching_networks = [
                        net
                        for net in active_networks
                        if net.version == test_net.version
                    ]
                    # Cast to ensure type checker knows test_net matches the network types
                    if isinstance(test_net, ipaddress.IPv4Network):
                        if all(
                            isinstance(net, ipaddress.IPv4Network)
                            and net.subnet_of(test_net)
                            for net in matching_networks
                        ):
                            return str(test_net)
                    else:
                        if all(
                            isinstance(net, ipaddress.IPv6Network)
                            and net.subnet_of(test_net)
                            for net in matching_networks
                        ):
                            return str(test_net)

            return None

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def subnet_overlap_check(subnet1: str, subnet2: str) -> dict:
    """
    Check if two subnets overlap.

    Use case: Preventing IP conflicts, network design validation.

    Args:
        subnet1: First subnet in CIDR notation
        subnet2: Second subnet in CIDR notation

    Returns:
        Dictionary with overlap status and details
    """
    try:
        net1 = ipaddress.ip_network(subnet1, strict=False)
        net2 = ipaddress.ip_network(subnet2, strict=False)

        # Check if networks are same version before comparing
        if net1.version != net2.version:
            return {
                "error": "Cannot compare subnets of different IP versions",
                "subnet1": str(net1),
                "subnet2": str(net2),
            }

        overlaps = net1.overlaps(net2)

        # Type narrowing for subnet_of calls
        if isinstance(net1, ipaddress.IPv4Network) and isinstance(
            net2, ipaddress.IPv4Network
        ):
            subnet1_contains_subnet2 = net2.subnet_of(net1)
            subnet2_contains_subnet1 = net1.subnet_of(net2)
        elif isinstance(net1, ipaddress.IPv6Network) and isinstance(
            net2, ipaddress.IPv6Network
        ):
            subnet1_contains_subnet2 = net2.subnet_of(net1)
            subnet2_contains_subnet1 = net1.subnet_of(net2)
        else:
            subnet1_contains_subnet2 = False
            subnet2_contains_subnet1 = False

        return {
            "overlap": overlaps,
            "subnet1": str(net1),
            "subnet2": str(net2),
            "subnet1_contains_subnet2": subnet1_contains_subnet2,
            "subnet2_contains_subnet1": subnet2_contains_subnet1,
        }

    except ValueError as e:
        return {"error": str(e)}


def subnet_into_smaller_subnets(cidr: str, new_prefix: int) -> List[str]:
    """
    Divide a subnet into smaller subnets.

    Use case: Network segmentation, VLAN planning, microservices isolation.

    Args:
        cidr: Original subnet in CIDR notation
        new_prefix: New prefix length (must be larger than original)

    Returns:
        List of smaller subnets
    """
    try:
        network = ipaddress.ip_network(cidr, strict=False)

        if new_prefix <= network.prefixlen:
            raise ValueError(
                f"New prefix {new_prefix} must be larger than current {network.prefixlen}"
            )

        subnets = list(network.subnets(new_prefix=new_prefix))
        return [str(subnet) for subnet in subnets]

    except ValueError as e:
        print(f"Error: {e}")
        return []


def analyze_network_logs(log_file: Path, subnet_filter: Optional[str] = None) -> dict:
    """
    Analyze network logs and extract IP-based insights.

    Use case: Security analysis, traffic pattern identification.

    Args:
        log_file: Path to CSV log file with 'ip_address' column
        subnet_filter: Optional subnet to filter results

    Returns:
        Dictionary with analysis results
    """
    ip_counts = {}
    unique_ips = set()
    private_ips = 0
    public_ips = 0

    try:
        # Note: This is a demonstration - adjust based on actual log format
        # Assuming CSV with headers including 'ip_address'
        if log_file.exists():
            with open(log_file, "r") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    ip_str = row.get("ip_address", "").strip()

                    try:
                        ip = ipaddress.ip_address(ip_str)

                        # Apply subnet filter if provided
                        if subnet_filter:
                            network = ipaddress.ip_network(subnet_filter, strict=False)
                            if ip not in network:
                                continue

                        unique_ips.add(str(ip))
                        ip_counts[str(ip)] = ip_counts.get(str(ip), 0) + 1

                        if ip.is_private:
                            private_ips += 1
                        else:
                            public_ips += 1

                    except ValueError:
                        continue

        # Get top 10 IPs by frequency
        top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        return {
            "total_unique_ips": len(unique_ips),
            "private_ip_count": private_ips,
            "public_ip_count": public_ips,
            "top_10_ips": dict(top_ips),
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    print("=== IP Address Validation ===")
    test_ips = ["192.168.1.1", "256.1.1.1", "2001:db8::1", "invalid"]
    for ip in test_ips:
        is_valid, ip_type = validate_ip_address(ip)
        print(f"{ip}: Valid={is_valid}, Type={ip_type}")

    print("\n=== IP Categorization ===")
    sample_ips = ["192.168.1.1", "8.8.8.8", "127.0.0.1", "224.0.0.1", "10.0.0.1"]
    categories = categorize_ip_addresses(sample_ips)
    for category, ips in categories.items():
        if ips:
            print(f"{category}: {ips}")

    print("\n=== Subnet Information ===")
    subnet_info = calculate_subnet_info("10.0.0.0/24")
    for key, value in subnet_info.items():
        print(f"{key}: {value}")

    print("\n=== Subnet Division ===")
    smaller_subnets = subnet_into_smaller_subnets("10.0.0.0/24", 26)
    print(f"Divided into {len(smaller_subnets)} subnets:")
    for subnet in smaller_subnets[:4]:  # Show first 4
        print(f"  {subnet}")

    print("\n=== Overlap Check ===")
    overlap = subnet_overlap_check("192.168.1.0/24", "192.168.1.128/25")
    print(f"Overlap result: {overlap}")
