"""3697. Compute Decimal Representation"""

from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        out: list[int] = []

        base: int = 1

        while n > 0:
            div, mod = divmod(n, 10)

            if mod:
                out.append(mod * base)

            base *= 10

            n = div

        return out[::-1]
