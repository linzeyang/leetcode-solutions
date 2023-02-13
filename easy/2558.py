"""2558. Take Gifts From the Richest Pile"""

from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts = sorted(gifts)
            num = gifts[-1]
            gifts.pop()
            gifts.append(int(num ** 0.5))

        return sum(gifts)
