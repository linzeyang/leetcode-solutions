"""1672. Richest Customer Wealth"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return sum(sorted(accounts, key=sum)[-1])
