"""
3120. Count the Number of Special Characters I

https://leetcode.com/problems/count-the-number-of-special-characters-i/

Weekly Contest 394
"""

from collections import Counter


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter: Counter[str] = Counter(word)

        out: int = 0

        for key in counter.keys():
            if key.islower() and key.upper() in counter:
                out += 1

        return out
