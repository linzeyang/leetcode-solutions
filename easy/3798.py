"""3798. Largest Even Number"""


class Solution:
    def largestEven(self, s: str) -> str:
        for idx in range(1, len(s) + 1):
            if s[-idx] == "2":
                return s[: len(s) - idx + 1]

        return ""
