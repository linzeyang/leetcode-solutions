"""
1833. Maximum Ice Cream Bars

https://leetcode.com/problems/maximum-ice-cream-bars/

Weekly Contest 237
"""

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        total: int = 0
        num: int = 0

        for cost in costs:
            total += cost

            if total > coins:
                break

            num += 1

        return num
