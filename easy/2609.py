"""2609. Find the Longest Balanced Substring of a Binary String"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        sub = False
        zeros = ones = 0
        out = 0

        for idx, char in enumerate(s):
            if not sub:
                if char == "0":
                    sub = True
                    zeros += 1
            elif char == "1":
                ones += 1
            elif s[idx - 1] == "0":
                zeros += 1
            else:
                out = max(out, min(zeros, ones) * 2)
                zeros, ones = 1, 0

        if sub and char == "1":
            out = max(out, min(zeros, ones) * 2)

        return out
