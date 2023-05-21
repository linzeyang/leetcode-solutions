"""2697. Lexicographically Smallest Palindrome"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        out: list[str] = []

        for idx in range(len(s) // 2):
            if s[idx] == s[-idx - 1]:
                out.append(s[idx])
            else:
                out.append(min(s[idx], s[-idx - 1]))

        if len(s) % 2 != 0:
            out = out + [s[len(s) // 2]] + out[::-1]
        else:
            out = out + out[::-1]

        return "".join(out)
