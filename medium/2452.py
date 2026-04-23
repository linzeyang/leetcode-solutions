"""
2452. Words Within Two Edits of Dictionary

https://leetcode.com/problems/words-within-two-edits-of-dictionary/

Biweekly Contest 90
"""

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        out: list[str] = []

        for word in queries:
            for candidate in dictionary:
                diffs: int = 0

                for idx, char in enumerate(word):
                    if char != candidate[idx]:
                        diffs += 1
                        if diffs > 2:
                            break
                else:
                    out.append(word)
                    break

        return out
