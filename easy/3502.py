"""3502. Minimum Cost to Reach Every Position"""

from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        out: list[int] = [cost[0]]

        for idx in range(1, len(cost)):
            out.append(min(cost[idx], out[-1]))

        return out
