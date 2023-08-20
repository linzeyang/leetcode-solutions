"""2828. Check if a String Is an Acronym of Words"""

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == "".join(word[0] for word in words)
