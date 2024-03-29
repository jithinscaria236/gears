#!/usr/bin/env python
from typing import List
from netaddr import IPNetwork, IPSet


class PrefixLargerThanCidrs(ValueError):
    pass


def consolidate_cidrs(cidrs: List[str]) -> List[str]:
    return [str(nw) for nw in IPSet(cidrs).iter_cidrs()]


def remove_used_cidrs(all_cidrs: List[str], used_cidrs: List[str]) -> List[str]:
    all_cidrs = IPSet(all_cidrs)
    for nw in used_cidrs:
        all_cidrs.remove(IPNetwork(nw))
    return [str(nw) for nw in all_cidrs.iter_cidrs()]


def allocate_cidr(all_cidrs: List[str], prefix: int) -> str:
    cidrs = IPSet(all_cidrs)
    for cidr in cidrs.iter_cidrs():
        try:
            return str(list(cidr.subnet(prefix))[0])
        except Exception as err:
            # cidr cannot accomodate prefix
            print(err)
            pass
    else:
        # Ref: https://docs.python.org/3/reference/simple_stmts.html#raise
        raise PrefixLargerThanCidrs({"prefix": prefix, "cidrs": cidrs})
