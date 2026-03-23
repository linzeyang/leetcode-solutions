"""
3876. Construct Uniform Parity Array II

https://leetcode.com/problems/construct-uniform-parity-array-ii/

Weekly Contest 494
"""


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd: int | None = None
        min_even: int | None = None

        for num in nums1:
            if num & 1:
                if min_odd is None or num < min_odd:
                    min_odd = num
            else:
                if min_even is None or num < min_even:
                    min_even = num

        return not min_odd or not min_even or min_even > min_odd
