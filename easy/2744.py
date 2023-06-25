"""2744. Find Maximum Number of String Pairs"""

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        temp = set()
        out = 0

        for word in words:
            if (target := word[::-1]) in temp:
                out += 1
                temp.remove(target)
            else:
                temp.add(word)

        return out
