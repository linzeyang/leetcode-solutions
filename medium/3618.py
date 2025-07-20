"""3618. Split Array by Prime Indices"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 2:
            return abs(sum(nums))

        idxs: list[int] = [1] * length

        idxs[0] = 0
        idxs[1] = 0

        for idx in range(4, length, 2):
            idxs[idx] = 0

        for odd in range(3, length // 3 + 1, 2):
            mul = 3

            while odd * mul < length:
                idxs[odd * mul] = 0
                mul += 2

        primes = sum(nums[idx] for idx, res in enumerate(idxs) if res)
        no_primes = sum(nums[idx] for idx, res in enumerate(idxs) if not res)

        return abs(primes - no_primes)
