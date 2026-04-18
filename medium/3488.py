"""
3488. Closest Equal Element Queries

https://leetcode.com/problems/closest-equal-element-queries/

Weekly Contest 441
"""

from bisect import bisect_left
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_to_indices: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            num_to_indices.setdefault(num, []).append(idx)

        out: list[int] = []

        for query in queries:
            candidates: list[int] = num_to_indices[nums[query]]

            if len(candidates) == 1:
                out.append(-1)
                continue

            pos: int = bisect_left(candidates, query)
            prev_idx: int = candidates[pos - 1] if pos > 0 else candidates[-1]
            next_idx: int = (
                candidates[pos + 1] if pos < len(candidates) - 1 else candidates[0]
            )

            prev_dist: int = abs(query - prev_idx)
            next_dist: int = abs(query - next_idx)

            out.append(
                min(prev_dist, len(nums) - prev_dist, next_dist, len(nums) - next_dist)
            )

        return out
