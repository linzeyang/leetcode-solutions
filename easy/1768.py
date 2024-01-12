"""1768. Merge Strings Alternately"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out: list[str] = []

        idx = 0

        while idx < min(len(word1), len(word2)):
            out.append(word1[idx])
            out.append(word2[idx])
            idx += 1

        if idx < len(word1):
            out.append(word1[idx:])
        elif idx < len(word2):
            out.append(word2[idx:])

        return "".join(out)
