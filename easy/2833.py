"""
2833. Furthest Point From Origin

https://leetcode.com/problems/furthest-point-from-origin/

Weekly Contest 360
"""

from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter: Counter[str] = Counter(moves)

        return abs(counter["L"] - counter["R"]) + counter["_"]
