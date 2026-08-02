"""
3517. Smallest Palindromic Rearrangement I

https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

Weekly Contest 445
"""

from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length: int = len(s)

        if length <= 2:
            return s

        mid: str = s[length // 2] if length & 1 else ""

        counter: Counter[str] = Counter(s[: length // 2])

        left: str = "".join(char * counter[char] for char in sorted(counter.keys()))
        right: str = left[::-1]

        return left + mid + right
