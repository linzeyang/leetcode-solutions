"""1486. XOR Operation in an Array"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        out = start

        for i in range(start + 2, start + 2 * n, 2):
            out ^= i

        return out
