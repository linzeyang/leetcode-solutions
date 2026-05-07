"""
3918. Sum of Primes Between Number and Its Reverse

https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

Weekly Contest 500
"""


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r: int = int(str(n)[::-1])

        lower: int = min(n, r)
        upper: int = max(n, r)

        def is_prime(number: int) -> bool:
            if number == 1:
                return False

            if number in {2, 3, 5, 7, 11, 13, 17, 19}:
                return True

            if number & 1 == 0:
                return False

            for factor in range(3, int(number**0.5) + 1, 2):
                if number % factor == 0:
                    return False

            return True

        out: int = 0

        for number in range(lower, upper + 1):
            if is_prime(number):
                out += number

        return out
