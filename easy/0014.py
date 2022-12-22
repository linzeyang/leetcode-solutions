""" 14. Longest Common Prefix """

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = []

        for i in range(min(len(s) for s in strs)):
            char = strs[0][i]

            if all(char == s[i] for s in strs[1:]):
                out.append(char)
            else:
                break

        return "".join(out)
