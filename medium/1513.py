"""1513. Number of Substrings With Only 1s"""


class Solution:
    def numSub(self, s: str) -> int:
        out = current = 0

        for char in s:
            if char == "1":
                current += 1
            elif current:
                out += (current + 1) * current // 2
                current = 0

        if current:
            out += (current + 1) * current // 2

        return out % (int(1e9 + 7))
