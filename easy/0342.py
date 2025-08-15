"""342. Power of Four"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        if n % 4 != 0:
            return False

        return self.isPowerOfFour(n // 4)


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        bin_str: str = bin(n)[2:]

        return bin_str.count("1") == 1 and (len(bin_str) - 1) % 2 == 0
