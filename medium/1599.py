"""1599. Maximum Profit of Operating a Centennial Wheel"""

from typing import List


class Solution:
    def minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int
    ) -> int:
        best = num = best_profit = profit = remaining = 0

        for customer in customers:
            on_board = min(remaining + customer, 4)
            remaining = remaining + customer - on_board
            profit += boardingCost * on_board - runningCost

            num += 1

            if profit > best_profit:
                best_profit = profit
                best = num

        while remaining > 0:
            on_board = min(remaining, 4)
            remaining = remaining - on_board
            profit += boardingCost * on_board - runningCost

            num += 1

            if profit > best_profit:
                best_profit = profit
                best = num

        if best == 0:
            return -1

        return best
