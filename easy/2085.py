"""2085. Count Common Words With One Occurrence"""

from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        out = 0

        for word, count in counter1.items():
            if count == 1 and counter2.get(word, 0) == 1:
                out += 1

        return out
