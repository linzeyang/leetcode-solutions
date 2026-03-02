"""3856. Trim Trailing Vowels"""


class Solution:
    """
    https://leetcode.com/problems/trim-trailing-vowels/
    Weekly Contest 491
    """

    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip("aeiou")


class Solution2:
    def trimTrailingVowels(self, s: str) -> str:
        for idx in range(1, len(s) + 1):
            if s[-idx] not in "aeiou":
                break
        else:
            return ""

        return s[: len(s) - idx + 1]
