"""1561. Maximum Number of Coins You Can Get"""

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[-idx * 2] for idx in range(1, len(piles) // 3 + 1))
