"""
3979. Maximum Valid Pair Sum

https://leetcode.com/problems/maximum-valid-pair-sum/

Biweekly Contest 186
"""


class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        suffix_sums: list[int] = [nums[-1]]

        for idx in range(2, len(nums)):
            suffix_sums.append(max(suffix_sums[-1], nums[-idx]))

        out: int = 0

        for idx in range(len(nums) - k):
            a: int = nums[idx]
            b: int = suffix_sums[len(nums) - idx - k - 1]

            out = max(out, a + b)

        return out
