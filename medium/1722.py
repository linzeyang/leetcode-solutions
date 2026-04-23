"""
1722. Minimize Hamming Distance After Swap Operations

https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

Weekly Contest 223
"""

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n

    def find(self, x: int) -> int:
        """
        Find the root of x.
        """

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Union x and y.
        """

        x_root: int = self.find(x)
        y_root: int = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        union_find: UnionFind = UnionFind(len(source))

        for x, y in allowedSwaps:
            union_find.union(x, y)

        mapping: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))

        for idx, num in enumerate(source):
            parent: int = union_find.find(idx)
            mapping[parent][num] += 1
            mapping[parent][target[idx]] -= 1

        out: int = 0

        for counts in mapping.values():
            for count in counts.values():
                if count > 0:
                    out += count

        return out
