"""
4061. Minimum Queen Moves to Reach Target

https://leetcode.com/problems/minimum-queen-moves-to-reach-target/

Biweely Contest 192
"""


class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target:
            return 0

        if (
            source[0] == target[0]
            or source[1] == target[1]
            or abs(source[0] - target[0]) == abs(source[1] - target[1])
        ):
            return 1

        return 2
