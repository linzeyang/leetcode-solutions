"""744. Find Smallest Letter Greater Than Target"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ss = set(letters)

        for char in sorted(ss):
            if char > target:
                return char

        return letters[0]
