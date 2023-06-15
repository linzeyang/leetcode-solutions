"""347. Top K Frequent Elements"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cc = Counter(nums)

        return sorted(cc.keys(), key=lambda num: cc[num], reverse=True)[:k]
