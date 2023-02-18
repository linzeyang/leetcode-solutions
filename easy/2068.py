"""2068. Check Whether Two Strings are Almost Equivalent"""

from collections import Counter
from string import ascii_lowercase


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        for letter in ascii_lowercase:
            if abs(counter1.get(letter, 0) - counter2.get(letter, 0)) > 3:
                return False

        return True
