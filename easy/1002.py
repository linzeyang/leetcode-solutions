"""1002. Find Common Characters"""

from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words)

        return list(reduce(self._find_common, words))

    def _find_common(self, word1: str, word2: str) -> str:
        common_chars = set(word1) & set(word2)

        cc1 = Counter(word1)
        cc2 = Counter(word2)

        return "".join(char * min(cc1[char], cc2[char]) for char in common_chars)
