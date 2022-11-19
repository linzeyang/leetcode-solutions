"""409. Longest Palindrome"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cc = Counter(s)
        out = 0
        has_odd = False

        for count in cc.values():
            if count % 2 == 0:
                out += count
            else:
                has_odd = True
                out += count - 1

        return out + has_odd
