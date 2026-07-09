"""
1967. Number of Strings That Appear as Substrings in Word

https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

Weekly Contest 254
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for pattern in patterns if pattern in word)
