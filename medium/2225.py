"""2225. Find Players With Zero or One Losses"""

from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lis1 = sorted({win for win, _ in matches} - {lose for _, lose in matches})

        cc = Counter(lose for _, lose in matches)

        lis2 = sorted(lose for lose, count in cc.items() if count == 1)

        return [lis1, lis2]
