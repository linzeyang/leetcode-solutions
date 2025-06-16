"""1446. Consecutive Characters"""


class Solution:
    def maxPower(self, s: str) -> int:
        out = sub = 1

        for idx in range(1, len(s)):
            if s[idx] == s[idx - 1]:
                sub += 1
            else:
                out = max(out, sub)
                sub = 1

        return max(out, sub)
