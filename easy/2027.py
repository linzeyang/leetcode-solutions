"""2027. Minimum Moves to Convert String"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        if "X" not in s:
            return 0

        out = idx = 0

        while idx < len(s):
            if s[idx] == "O":
                idx += 1
            else:
                out += 1
                idx += 3

        return out
