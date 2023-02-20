"""2144. Minimum Cost of Buying Candies With Discount"""

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)

        cost = sorted(cost, reverse=True)

        out = idx = 0

        while idx < len(cost):
            try:
                out += cost[idx] + cost[idx + 1]
            except IndexError:
                out += cost[idx]
                break

            idx += 3

        return out
