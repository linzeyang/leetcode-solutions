"""744. Find Smallest Letter Greater Than Target"""

from bisect import bisect
from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-smallest-letter-greater-than-target/
    Weekly Contest 62
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Linear Search
        for letter in letters:
            if letter > target:
                break
        else:
            return letters[0]

        return letter


class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Binary Search, more efficient
        if letters[-1] <= target:
            return letters[0]

        return letters[bisect(letters, target)]
