"""3813. Vowel-Consonant Score"""

from math import floor


class Solution:
    """
    https://leetcode.com/problems/vowel-consonant-score/description/
    Weekly Contest 485
    """

    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0

        for char in s:
            if char.isdigit() or char == " ":
                continue
            if char in "aeiou":
                v += 1
            else:
                c += 1

        return floor(v / c) if c else 0
