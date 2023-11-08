"""2914. Minimum Number of Changes to Make Binary String Beautiful"""


class Solution:
    def minChanges(self, s: str) -> int:
        out = 0

        for idx in range(0, len(s), 2):
            if s[idx] != s[idx + 1]:
                out += 1

        return out
