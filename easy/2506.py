"""2506. Count Pairs Of Similar Strings"""

from itertools import combinations
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        out = 0

        for s1, s2 in combinations((set(word) for word in words), 2):
            if s1 == s2:
                out += 1

        return out
