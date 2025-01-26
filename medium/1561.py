"""1561. Maximum Number of Coins You Can Get"""

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        return sum(piles[idx * 2 + 1] for idx in range(len(piles) // 3))
