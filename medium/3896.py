"""
3896. Minimum Operations to Transform Array into Alternating Prime

https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

Biweekly Contest 180
"""

known_primes: set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}


class Solution:
    def minOperations(self, nums: list[int]) -> int:

        def is_prime(n: int) -> bool:
            if n == 1:
                return False

            if n in known_primes:
                return True

            if n & 1 == 0:
                return False

            for factor in range(3, int(n**0.5) + 1, 2):
                if n % factor == 0:
                    return False

            known_primes.add(n)
            return True

        def next_prime(n: int) -> int:
            target: int = n + 1

            while not is_prime(target):
                if target & 1:
                    target += 2
                else:
                    target += 1

            return target

        out: int = 0

        for idx, num in enumerate(nums):
            if idx & 1 == 0 and not is_prime(num):
                out += next_prime(num) - num

            elif idx & 1 and is_prime(num):
                out += 2 if num == 2 else 1

        return out
