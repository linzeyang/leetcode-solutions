"""
344. Reverse String
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Slow:
        # Runtime: 491 ms, faster than 8.64% of Python3 online submissions for Reverse String.
        # Memory Usage: 18.4 MB, less than 43.35% of Python3 online submissions for Reverse String.
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
