"""
3974. Maximum Total Sum of K Selected Elements

https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

Weekly Contest 508
"""


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)

        out: int = 0

        for idx in range(k):
            if mul > 1:
                out += nums[idx] * mul
                mul -= 1
            else:
                out += nums[idx]

        return out
