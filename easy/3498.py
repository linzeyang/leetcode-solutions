"""3498. Reverse Degree of a String"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        out = 0

        for idx, char in enumerate(s):
            out += (26 - ord(char) + ord("a")) * (idx + 1)

        return out
