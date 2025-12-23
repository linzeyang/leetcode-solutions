"""3784. Minimum Deletion Cost to Make All Characters Equal"""

from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        char_cost: dict[str, int] = {}

        for char, cos in zip(s, cost, strict=True):
            if char not in char_cost:
                char_cost[char] = cos
            else:
                char_cost[char] += cos

        return sum(cost) - max(char_cost.values())
