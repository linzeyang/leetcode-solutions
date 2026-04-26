"""
2615. Sum of Distances

https://leetcode.com/problems/sum-of-distances/

Weekly Contest 340
"""

from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_indices: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            num_indices.setdefault(num, []).append(idx)

        out: list[int] = [0] * len(nums)

        for indices in num_indices.values():
            if len(indices) == 1:
                continue

            total_sum: int = sum(indices)
            left_sum = 0
            k: int = len(indices)

            for i, idx in enumerate(indices):
                right_sum: int = total_sum - left_sum - idx
                out[idx] = i * idx - left_sum + right_sum - (k - 1 - i) * idx
                left_sum += idx

        return out
