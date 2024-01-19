"""387. First Unique Character in a String"""

from string import ascii_lowercase


class Solution:
    def firstUniqChar(self, s: str) -> int:
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
