"""2303. Calculate Amount Paid in Taxes"""

from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        out: float = 0
        last_upper = 0

        for item in brackets:
            upper, percent = item
            inter_upper = upper - last_upper

            if income <= inter_upper:
                out += income * percent / 100
                break

            out += inter_upper * percent / 100
            income -= inter_upper
            last_upper = upper

        return out
