"""
4014. Minimum Total Price After Applying Discounts

https://leetcode.com/problems/minimum-total-price-after-applying-discounts/

Weekly Contest 514
"""


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        out: float = 0.0

        for idx in range(min(len(prices), len(discounts))):
            out += prices[idx] * (1 - discounts[idx] / 100)

        for jdx in range(idx + 1, len(prices)):
            out += prices[jdx]

        return round(out, 5)
