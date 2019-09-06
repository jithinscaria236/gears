import pytest
import ip_mgmt_examples as ip


# Test consolidate_cidrs function
data_consolidate = [
    ("simple-0", ['10.0.0.0/24'], ['10.0.0.0/24']),
    ("simple-1", ['10.0.0.0/24', '10.0.1.0/24'], ['10.0.0.0/23']),
    ("simple-2", ['10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24'], ['10.0.0.0/23', '10.0.2.0/24']),
    ("simple-3", ['10.0.0.0/32', '10.0.0.1/32', '10.0.0.2/32', '10.0.0.3/32', '10.0.0.4/32', '10.0.0.5/32'],
     ['10.0.0.0/30', '10.0.0.4/31']),
    ("simple-4", [], [])
]


@pytest.mark.parametrize(
    "id,cidrs,expected",
    data_consolidate,
    ids=[i[0] for i in data_consolidate]
)
def test_cosolidate(id, cidrs, expected):
    result = ip.consolidate_cidrs(cidrs)
    assert result == expected


# Test remove_used_cidrs function
data_remove_used = [
    ("simple-0", [], [], []),
    ("simple-1", ['10.0.0.0/32'], ['10.0.0.0/32'], []),
    ("simple-2", ['10.0.0.0/31'], ['10.0.0.0/32'], ['10.0.0.1/32']),
    ("simple-3", ['10.0.0.0/30'], ['10.0.0.0/32'], ['10.0.0.1/32', '10.0.0.2/31']),
]


@pytest.mark.parametrize(
    "id,all_cidrs,used_cidrs,expected",
    data_remove_used,
    ids=[i[0] for i in data_remove_used]
)
def test_remove_used_cidrs(id, all_cidrs, used_cidrs, expected):
    result = ip.remove_used_cidrs(all_cidrs, used_cidrs)
    assert result == expected


# Test allocate_cidrs
data_allocate_cidrs = [
    ("simple-1", ['10.0.0.0/23'], 24, '10.0.0.0/24'),
    ("simple-2", ['10.0.0.0/24', '10.0.2.0/23'], 23, '10.0.2.0/23')
]


@pytest.mark.parametrize(
    "id,all_cidrs,prefix,expected",
    data_allocate_cidrs,
    ids=[i[0] for i in data_allocate_cidrs]
)
def test_allocate_cidr(id, all_cidrs, prefix, expected):
    result = ip.allocate_cidr(all_cidrs, prefix)
    assert result == expected


def test_remove_unused_cidrs_exception():
    with pytest.raises(ip.PrefixLargerThanCidrs):
        ip.allocate_cidr([], 23)
