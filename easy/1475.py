"""1475. Final Prices With a Special Discount in a Shop"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out = []

        for i in range(len(prices) - 1):
            a = prices[i]

            for j in range(i + 1, len(prices)):
                if (b := prices[j]) <= a:
                    out.append(a - b)
                    break
            else:
                out.append(a)

        out.append(prices[-1])

        return out
