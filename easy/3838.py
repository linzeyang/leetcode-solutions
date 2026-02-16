"""3838. Weighted Word Mapping"""

from string import ascii_lowercase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/weighted-word-mapping/
    Biweekly Contest 176
    """

    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapping1: dict[str, int] = dict(zip(ascii_lowercase, weights, strict=True))

        def weight(word: str) -> int:
            return sum(mapping1[char] for char in word) % 26

        mapping2: str = ascii_lowercase[::-1]

        return "".join(mapping2[weight(word)] for word in words)
