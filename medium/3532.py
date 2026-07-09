"""
3532. Path Existence Queries in a Graph I

https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

Weekly Contest 447
"""

from bisect import bisect_right
from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        groups: list[int] = [0]

        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx - 1] > maxDiff:
                groups.append(idx)

        return [bisect_right(groups, a) == bisect_right(groups, b) for a, b in queries]
