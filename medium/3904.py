"""
3904. Smallest Stable Index II

https://leetcode.com/problems/smallest-stable-index-ii/

Weekly Contest 498
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        backward_min: list[int] = []

        for num in reversed(nums):
            if not backward_min:
                backward_min.append(num)
            else:
                backward_min.append(min(num, backward_min[-1]))

        current_max: int = 0

        for idx, num in enumerate(nums):
            current_max = max(current_max, num)

            if current_max - backward_min[-idx - 1] <= k:
                return idx

        return -1
