"""2347. Best Poker Hand"""

from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_c = Counter(ranks)
        suit_c = Counter(suits)

        if len(suit_c) == 1:
            return "Flush"

        if (maxx := max(rank_c.values())) >= 3:
            return "Three of a Kind"

        if maxx == 2:
            return "Pair"

        return "High Card"
