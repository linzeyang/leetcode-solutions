"""3517. Smallest Palindromic Rearrangement I"""


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)

        if length & 1:
            mid = s[length // 2]
        else:
            mid = ""

        left = sorted(s[: length // 2])
        right = left[::-1]

        return "".join(left + [mid] + right)
