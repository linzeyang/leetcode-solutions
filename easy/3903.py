"""
3903. Smallest Stable Index I

https://leetcode.com/problems/smallest-stable-index-i/

Weekly Contest 498
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        forward_max: list[int] = []
        backward_min: list[int] = []

        for num in nums:
            if not forward_max:
                forward_max.append(num)
            else:
                forward_max.append(max(num, forward_max[-1]))

        for num in reversed(nums):
            if not backward_min:
                backward_min.append(num)
            else:
                backward_min.append(min(num, backward_min[-1]))

        for idx in range(len(nums)):
            if forward_max[idx] - backward_min[-idx - 1] <= k:
                return idx

        return -1
