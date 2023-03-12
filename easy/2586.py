"""2586. Count the Number of Vowel Strings in Range"""

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        out = 0
        vowels = {"a", "e", "i", "o", "u"}

        for idx in range(left, right + 1):
            if words[idx][0] in vowels and words[idx][-1] in vowels:
                out += 1

        return out
