"""
4062. Transform Array Using Pair Operations

https://leetcode.com/problems/transform-array-using-pair-operations/

Biweely Contest 192
"""


class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        return sum(source) == sum(target)
