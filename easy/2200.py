"""2200. Find All K-Distant Indices in an Array"""

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx = lower = 0
        out = []
        max_idx = len(nums) - 1

        while idx < len(nums):
            if nums[idx] == key:
                lower = max(0, lower, idx - k)
                upper = min(max_idx, idx + k)
                out.extend(list(range(lower, upper + 1)))
                lower = upper + 1
            idx += 1

        return out
