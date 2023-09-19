"""1544. Make The String Great"""


class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s

        while s:
            for idx in range(len(s) - 1):
                if s[idx].swapcase() == s[idx + 1]:
                    s = s.replace(s[idx : idx + 2], "")
                    break
            else:
                break

        return s
