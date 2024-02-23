"""3042. Count Prefix and Suffix Pairs I"""

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(
            1
            for idx in range(len(words) - 1)
            for jdx in range(idx + 1, len(words))
            if words[jdx].startswith(words[idx]) and words[jdx].endswith(words[idx])
        )
