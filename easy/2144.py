"""
2144. Minimum Cost of Buying Candies With Discount

https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

Biweekly Contest 70
"""

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        return sum(candy for idx, candy in enumerate(cost) if idx % 3 != 2)
