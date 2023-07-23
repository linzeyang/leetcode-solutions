"""2788. Split Strings by Separator"""

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        out = []

        for word in words:
            out.extend([part for part in word.split(separator) if part])

        return out
