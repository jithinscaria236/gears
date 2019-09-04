#!/usr/bin/env python
from typing import List
from netaddr import IPNetwork, cidr_merge, IPSet


def consolidate_cidrs(cidrs: List[str]) -> List[str]:
    return [str(nw) for nw in IPSet(cidrs).iter_cidrs()]


def remove_used_cidrs(all_cidrs: List[str], used_cidrs: List[str]) -> List[str]:
    all_cidrs = IPSet(all_cidrs)
    for nw in used_cidrs:
        all_cidrs.remove(IPNetwork(nw))
    return [str(nw) for nw in all_cidrs.iter_cidrs()]


if __name__ == "__main__":
    x = consolidate_cidrs(['192.168.0.0/24', '192.168.1.0/24'])
    print(x)
    from IPython import embed
    embed()

