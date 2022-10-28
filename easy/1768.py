"""1768. Merge Strings Alternately"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        comm = min(len(word1), len(word2))

        return "".join(
            [f"{word1[i]}{word2[i]}" for i in range(comm)]
            + [word1[comm:], word2[comm:]]
        )
