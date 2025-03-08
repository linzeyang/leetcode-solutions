"""2523. Closest Prime Numbers in Range"""

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.eratosthenes(left, right)

        if len(primes) < 2:
            return [-1, -1]

        diff = right - left

        out: list[int] = []

        for idx in range(1, len(primes)):
            if (new_diff := primes[-idx] - primes[-idx - 1]) <= diff:
                out = [primes[-idx - 1], primes[-idx]]
                diff = new_diff

        return out

    def eratosthenes(self, left, right) -> list[int]:
        """get all the primes within range [left, right]"""

        is_prime: list[bool] = [False, False] + [True] * right

        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        return [x for x in range(left, right + 1) if is_prime[x]]
