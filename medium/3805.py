"""3805. Count Caesar Cipher Pairs"""

from collections import Counter
from math import comb
from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        out: int = 0

        counter: Counter = Counter()

        for word in words:
            sig: tuple[int, ...] = tuple(
                (ord(word[idx]) - ord(word[idx - 1])) % 26
                for idx in range(1, len(word))
            )

            counter[sig] += 1

        for value in counter.values():
            out += comb(value, 2)

        return out
