"""
3982. Sum of Integers With Maximum Digit Range

https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

Weekly Contest 509
"""


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for num in nums:
            digits: list[int] = [int(char) for char in str(num)]
            diff: int = max(digits) - min(digits)

            mapping.setdefault(diff, []).append(num)

        return sum(mapping[max(mapping.keys())])
