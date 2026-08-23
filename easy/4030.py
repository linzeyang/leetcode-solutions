"""
4030. Check ASCII Palindromic

https://leetcode.com/problems/check-ascii-palindromic/

Weekly Contest 516
"""


class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary: str = "".join(f"{ord(char):0>8b}" for char in s)

        for idx in range(len(binary) // 2):
            if binary[idx] != binary[-idx - 1]:
                return False

        return True
