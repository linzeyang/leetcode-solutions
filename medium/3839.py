"""3839. Number of Prefix Connected Groups"""

from collections import Counter
from typing import List


class Solution:
    """
    https://leetcode.com/problems/number-of-prefix-connected-groups/
    Biweekly Contest 176
    """

    def prefixConnected(self, words: List[str], k: int) -> int:
        counter: Counter[str] = Counter(word[:k] for word in words if len(word) >= k)

        return sum(1 for val in counter.values() if val >= 2)
