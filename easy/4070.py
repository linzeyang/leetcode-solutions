"""
4070. Minimum Rotations to Dial a Number I

https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/

Weekly Contest 522
"""


class Solution:
    def minRotations(self, s: str) -> int:
        out: int = 0
        current: int = 0

        for char in s:
            destination: int = int(char)
            distance: int = abs(destination - current)

            out += distance if distance <= 5 else (10 - distance)

            current = destination

        return out
