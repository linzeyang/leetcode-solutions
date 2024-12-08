"""3304. Find the K-th Character in String Game I"""

from functools import lru_cache


class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            word += self._construct(word)

        return word[k - 1]

    def _construct(self, word: str) -> str:
        if len(word) == 1:
            return self._shift(word)

        return word[len(word) // 2 :] + self._construct(word[len(word) // 2 :])

    @lru_cache
    def _shift(self, char) -> str:
        return chr(ord(char) + 1) if char != "z" else "a"
