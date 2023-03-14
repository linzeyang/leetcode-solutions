"""1078. Occurrences After Bigram"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        out: list[str] = []
        words = text.split()

        for idx in range(len(words) - 2):
            if words[idx] == first and words[idx + 1] == second:
                out.append(words[idx + 2])

        return out
