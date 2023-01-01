"""2521. Distinct Prime Factors of Product of Array"""

import heapq
from typing import List


class Solution:
    known_primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
    ]

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        heapq.heapify(self.known_primes)

        existing_factors = set()

        for num in nums:
            for fac in self._find_prime_factors(num):
                existing_factors.add(fac)

        return len(existing_factors)

    def _find_prime_factors(self, num: int):
        while num > 1:
            if num in self.known_primes:
                yield num
                return

            for prime in self.known_primes:
                if num % prime == 0:
                    yield prime
                    num //= prime
                    break
            else:
                prime += 2
                while prime < num:
                    if num % prime == 0:
                        self.known_primes.append(prime)
                        num //= prime
                        break
                    prime += 2

                self.known_primes.append(num)
                yield num
                return
