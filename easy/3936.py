"""
3936. Minimum Swaps to Move Zeros to End

https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

Biweekly Contest 183
"""


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero_idxs: list[int] = []

        for idx, num in enumerate(nums):
            if num == 0:
                zero_idxs.append(idx)

        return sum(1 for idx in zero_idxs if idx < len(nums) - len(zero_idxs))
