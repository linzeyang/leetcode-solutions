"""2496. Maximum Value of a String in an Array"""

from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(self._get_value(word) for word in strs)

    @staticmethod
    def _get_value(word: str) -> int:
        if word.isdigit():
            return int(word)

        return len(word)
