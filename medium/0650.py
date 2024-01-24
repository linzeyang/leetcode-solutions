"""650. 2 Keys Keyboard"""


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        if n <= 5:
            return n

        for idx in range(2, int(n**0.5) + 1):
            if n % idx == 0:
                return self.minSteps(n // idx) + idx

        return n
