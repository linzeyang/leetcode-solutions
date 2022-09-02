"""
14. Longest Common Prefix
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min(len(s) for s in strs)

        out = ""

        for i in range(l):
            char = strs[0][i]
            if all_same(char, (s[i] for s in strs[1:])):
                out += char
            else:
                break

        return out


def all_same(letter, seq):
    for char in seq:
        if letter != char:
            return False

    return True
