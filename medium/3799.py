"""3799. Word Squares II"""

from itertools import permutations
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        out: list[list[str]] = []

        words_set: set[str] = set(words)

        for top in words_set:
            for left, right, bottom in permutations(words_set - {top}, 3):
                if (
                    top[0] == left[0]
                    and top[3] == right[0]
                    and left[3] == bottom[0]
                    and right[3] == bottom[3]
                ):
                    out.append([top, left, right, bottom])

        return sorted(out)
