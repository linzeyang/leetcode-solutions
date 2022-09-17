"""
387. First Unique Character in a String
"""
from string import ascii_lowercase


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Runtime: 168 ms, faster than 53.26% of Python3 online submissions for First Unique Character in a String.
        # Memory Usage: 14.2 MB, less than 16.71% of Python3 online submissions for First Unique Character in a String.

        out = {}
        ss = set(ascii_lowercase)

        for idx, char in enumerate(s):
            if char not in ss:
                continue

            if char not in out:
                out[char] = idx
            else:
                ss.remove(char)
                del out[char]

        for _, idx in out.items():
            return idx

        return -1
