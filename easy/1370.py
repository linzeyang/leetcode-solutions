"""1370. Increasing Decreasing String"""


class Solution:
    """
    https://leetcode.com/problems/increasing-decreasing-string/
    Biweekly Contest 21
    """

    def sortString(self, s: str) -> str:
        counts: list[int] = [0] * 26
        base: int = ord("a")

        for char in s:
            counts[ord(char) - base] += 1

        out: list[str] = []

        while len(out) < len(s):
            for i in range(26):
                if counts[i]:
                    out.append(chr(base + i))
                    counts[i] -= 1

            for i in range(25, -1, -1):
                if counts[i]:
                    out.append(chr(base + i))
                    counts[i] -= 1

        return "".join(out)
