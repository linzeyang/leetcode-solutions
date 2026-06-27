"""
3969. Valid Subarrays With Matching Sum Digits I

https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

Weekly Contest 507
"""


class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        out: int = 0
        strx: str = str(x)

        for idx in range(len(nums)):
            subarray_sum: int = 0

            for jdx in range(idx, len(nums)):
                subarray_sum += nums[jdx]

                str_sum: str = str(subarray_sum)

                if str_sum[0] == strx and str_sum[-1] == strx:
                    out += 1

        return out
