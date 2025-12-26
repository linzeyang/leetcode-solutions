"""3075. Maximize Happiness of Selected Children"""

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        return sum(max(happiness[turn] - turn, 0) for turn in range(k))
