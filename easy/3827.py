"""3827. Count Monobit Integers"""


class Solution:
    """
    https://leetcode.com/problems/count-monobit-integers/
    Weekly Contest 487
    """

    def countMonobit(self, n: int) -> int:
        out: int = 1
        num: int = 1

        while num <= n:
            out += 1
            num = (num << 1) + 1

        return out


class Solution2:
    def countMonobit(self, n: int) -> int:
        binary: str = bin(n)[2:]

        return len(binary) + ("0" in binary)
