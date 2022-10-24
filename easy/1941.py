"""1941. Check if All Characters Have Equal Number of Occurrences"""

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
