"""2652. Sum Multiples"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        if n < 3:
            return 0

        if n < 5:
            return 3

        return sum(
            num
            for num in range(1, n + 1)
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0
        )
