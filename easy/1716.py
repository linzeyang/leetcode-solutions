"""1716. Calculate Money in Leetcode Bank"""


class Solution:
    def totalMoney(self, n: int) -> int:
        x, y = divmod(n, 7)

        return (56 + 7 * (x - 1)) * x // 2 + (x * 2 + y + 1) * y // 2
