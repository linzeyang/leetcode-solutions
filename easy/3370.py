"""3370. Smallest Number With All Set Bits"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Bit manipulation
        Time complexity: O(log n)
        Space complexity: O(1)
        """

        out: int = 0

        while n:
            n >>= 1
            out = (out << 1) + 1

        return out
