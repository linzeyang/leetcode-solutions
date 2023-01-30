"""1160. Find Words That Can Be Formed by Characters"""

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = Counter(chars)
        out = 0

        for word in words:
            for char, count in Counter(word).items():
                if char not in cc or count > cc[char]:
                    break
            else:
                out += len(word)

        return out
