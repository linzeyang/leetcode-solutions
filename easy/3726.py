"""3726. Remove Zeros in Decimal Representation"""


class Solution:
    def removeZeros(self, n: int) -> int:
        out: list[str] = [char for char in str(n) if char != "0"]

        return int("".join(out))
