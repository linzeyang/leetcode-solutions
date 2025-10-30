"""3726. Remove Zeros in Decimal Representation"""


class Solution:
    def removeZeros(self, n: int) -> int:
        """
        String-based approach.
        - Simplicity: Very readable and intuitive - directly follows the description
        - Conciseness: Only 2 lines of actual logic
        - Clarity: Easy to understand what's happening at each step
        """

        out: list[str] = [char for char in str(n) if char != "0"]

        return int("".join(out))


class Solution2:
    def removeZeros(self, n: int) -> int:
        """
        Mathematical approach.
        - No string conversion: Works purely with mathematical operations
        - Potentially more efficient: Avoids string allocation and conversion overhead
        - Mathematical elegance: Uses digit extraction via modulo arithmetic
        """

        power: int = 0
        out: int = 0

        while n:
            n, mod = divmod(n, 10)

            if mod:
                out += mod * 10**power
                power += 1

        return out
