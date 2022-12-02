"""2485. Find the Pivot Integer"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        x = ((n**2 + n) / 2) ** 0.5

        return int(x) if not x % 1 else -1
