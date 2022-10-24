"""1967. Number of Strings That Appear as Substrings in Word"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([pre for pre in patterns if pre in word])
