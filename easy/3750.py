"""3750. Minimum Number of Flips to Reverse Binary String"""


class Solution:
    def minimumFlips(self, n: int) -> int:
        binary: str = bin(n)[2:]
        length: int = len(binary)

        return sum(
            2 for idx in range(length // 2) if binary[idx] != binary[length - idx - 1]
        )
