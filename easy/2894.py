"""2894. Divisible and Non-divisible Sums Difference"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0

        for num in range(1, n + 1):
            if num % m:
                num1 += num
            else:
                num2 += num

        return num1 - num2


class Solution2:
    def differenceOfSums(self, n: int, m: int) -> int:
        """sum of 1 to n substracts 2 times sum of m to K * m where K = n // m"""
        return (1 + n) * n // 2 - (m + n // m * m) * (n // m)
