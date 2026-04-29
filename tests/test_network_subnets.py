import ipaddress
import pytest
from network_subnets import (
    get_subnet_details,
    equal_capacity_subnets,
    specific_capacity_subnets,
    display_subnets,
)


# ---------------------------------------------------------------------------
# get_subnet_details
# ---------------------------------------------------------------------------

class TestGetSubnetDetails:
    def test_standard_slash24(self):
        net = ipaddress.ip_network("192.168.1.0/24")
        details = get_subnet_details(net)
        assert details["network"] == "192.168.1.0/24"
        assert details["network_address"] == "192.168.1.0"
        assert details["broadcast_address"] == "192.168.1.255"
        assert details["first_usable"] == "192.168.1.1"
        assert details["last_usable"] == "192.168.1.254"
        assert details["usable_hosts"] == 254
        assert details["subnet_mask"] == "255.255.255.0"

    def test_slash30(self):
        net = ipaddress.ip_network("10.0.0.0/30")
        details = get_subnet_details(net)
        assert details["usable_hosts"] == 2
        assert details["first_usable"] == "10.0.0.1"
        assert details["last_usable"] == "10.0.0.2"
        assert details["broadcast_address"] == "10.0.0.3"

    def test_slash32_no_usable_hosts(self):
        net = ipaddress.ip_network("10.0.0.1/32")
        details = get_subnet_details(net)
        # /32 has 1 "host" per ipaddress semantics
        assert details["usable_hosts"] == 1


# ---------------------------------------------------------------------------
# equal_capacity_subnets
# ---------------------------------------------------------------------------

class TestEqualCapacitySubnets:
    def test_split_into_4(self):
        results = equal_capacity_subnets("192.168.10.0/24", 4, verbose=False)
        assert len(results) == 4
        # All subnets should be /26
        for r in results:
            assert r["prefix_length"] == 26
            assert r["usable_hosts"] == 62

    def test_split_into_2(self):
        results = equal_capacity_subnets("10.0.0.0/24", 2, verbose=False)
        assert len(results) == 2
        assert results[0]["network"] == "10.0.0.0/25"
        assert results[1]["network"] == "10.0.0.128/25"

    def test_n_equals_1_returns_original(self):
        results = equal_capacity_subnets("10.0.0.0/24", 1, verbose=False)
        assert len(results) == 1
        assert results[0]["network"] == "10.0.0.0/24"

    def test_non_power_of_two_rounds_up(self):
        # 3 subnets → ceil(log2(3)) = 2 → 4 actual subnets
        results = equal_capacity_subnets("192.168.0.0/24", 3, verbose=False)
        assert len(results) == 4

    def test_prefix_overflow_raises(self):
        with pytest.raises(ValueError):
            equal_capacity_subnets("10.0.0.0/30", 16, verbose=False)

    def test_contiguous_subnets_cover_base(self):
        results = equal_capacity_subnets("172.16.0.0/20", 8, verbose=False)
        assert len(results) == 8
        networks = [ipaddress.ip_network(r["network"]) for r in results]
        # First subnet starts at base network address
        assert networks[0].network_address == ipaddress.ip_address("172.16.0.0")
        # Last subnet ends at broadcast of the /20
        base = ipaddress.ip_network("172.16.0.0/20")
        assert networks[-1].broadcast_address == base.broadcast_address


# ---------------------------------------------------------------------------
# specific_capacity_subnets (VLSM)
# ---------------------------------------------------------------------------

class TestSpecificCapacitySubnets:
    def test_basic_vlsm(self):
        results = specific_capacity_subnets("10.0.0.0/24", [50, 25, 10, 5], verbose=False)
        assert len(results) == 4
        for r, cap in zip(results, [50, 25, 10, 5]):
            assert r["requested_hosts"] == cap
            assert r["usable_hosts"] >= cap

    def test_subnets_do_not_overlap(self):
        results = specific_capacity_subnets("192.168.0.0/24", [100, 50, 20], verbose=False)
        networks = [ipaddress.ip_network(r["network"]) for r in results]
        for i, a in enumerate(networks):
            for j, b in enumerate(networks):
                if i != j:
                    assert not a.overlaps(b), f"{a} overlaps {b}"

    def test_all_subnets_within_base(self):
        base = ipaddress.ip_network("10.10.0.0/22")
        results = specific_capacity_subnets("10.10.0.0/22", [200, 100, 50], verbose=False)
        for r in results:
            subnet = ipaddress.ip_network(r["network"])
            assert base.supernet_of(subnet)

    def test_insufficient_space_raises(self):
        with pytest.raises(ValueError):
            specific_capacity_subnets("10.0.0.0/30", [200], verbose=False)

    def test_zero_or_negative_capacity_raises(self):
        with pytest.raises(ValueError):
            specific_capacity_subnets("10.0.0.0/24", [50, 0], verbose=False)

        with pytest.raises(ValueError):
            specific_capacity_subnets("10.0.0.0/24", [-1], verbose=False)

    def test_single_capacity(self):
        results = specific_capacity_subnets("192.168.1.0/24", [100], verbose=False)
        assert len(results) == 1
        assert results[0]["usable_hosts"] >= 100


# ---------------------------------------------------------------------------
# display_subnets
# ---------------------------------------------------------------------------

class TestDisplaySubnets:
    def test_returns_prettytable(self):
        from prettytable import PrettyTable
        results = equal_capacity_subnets("10.0.0.0/24", 2, verbose=False)
        table = display_subnets(results, title="Test Table", include_requested=False)
        assert isinstance(table, PrettyTable)

    def test_row_count_matches_subnets(self):
        results = equal_capacity_subnets("10.0.0.0/24", 4, verbose=False)
        table = display_subnets(results)
        # PrettyTable rows are accessible via the internal _rows attribute
        assert len(table.rows) == 4

    def test_requested_column_present_when_flag_set(self):
        results = specific_capacity_subnets("10.0.0.0/24", [30, 10], verbose=False)
        table = display_subnets(results, include_requested=True)
        assert "Requested" in table.field_names

    def test_requested_column_absent_by_default(self):
        results = equal_capacity_subnets("10.0.0.0/24", 2, verbose=False)
        table = display_subnets(results)
        assert "Requested" not in table.field_names
