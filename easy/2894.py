"""2894. Divisible and Non-divisible Sums Difference"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # return sum(range(1, n+1)) - 2 * sum(range(0, n + 1, m))

        num1 = num2 = 0

        for num in range(1, n + 1):
            if num % m:
                num1 += num
            else:
                num2 += num

        return num1 - num2
