"""
3925. Concatenate Array With Reverse

https://leetcode.com/problems/concatenate-array-with-reverse/

Weekly Contest 501
"""


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]
