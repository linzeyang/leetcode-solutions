"""2706. Buy Two Chocolates"""

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)

        return (
            money - summ
            if (summ := sorted_prices[0] + sorted_prices[1]) <= money
            else money
        )
