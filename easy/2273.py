"""2273. Find Resultant Array After Removing Anagrams"""

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words

        idx = -1

        while idx > -len(words):
            if len(words[idx]) == len(words[idx - 1]) and sorted(words[idx]) == sorted(
                words[idx - 1]
            ):
                words.pop(idx)
                idx = -1
                continue
            idx -= 1

        return words
