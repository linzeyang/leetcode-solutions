"""
4034. Minimum Bishop Moves to Reach Target

https://leetcode.com/problems/minimum-bishop-moves-to-reach-target/

Biweekly Contest 190
"""


class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        s1, s2 = source
        t1, t2 = target

        if (s1 + s2) & 1 != (t1 + t2) & 1:
            return -1

        return int(abs(t1 - s1) != abs(t2 - s2)) + 1
