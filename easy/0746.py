"""746. Min Cost Climbing Stairs"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lis: list[int] = []

        for idx, cos in enumerate(cost[::-1]):
            if idx < 2:
                lis.append(cos)
            else:
                lis.append(cos + min(lis[idx - 1], lis[idx - 2]))

        return min(lis[-1], lis[-2])
