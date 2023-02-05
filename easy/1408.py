"""1408. String Matching in an Array"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lis = sorted(words, key=len)
        out = []

        for idx in range(len(lis) - 1):
            for jdx in range(idx + 1, len(lis)):
                if lis[idx] in lis[jdx]:
                    out.append(lis[idx])
                    break

        return out
