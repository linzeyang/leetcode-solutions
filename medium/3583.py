"""3583. Count Special Triplets"""

from collections import Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counter_prev: Counter[int] = Counter(nums[:1])
        counter_after: Counter[int] = Counter(nums[2:])

        out: int = 0
        idx: int = 1

        while idx < len(nums) - 1:
            out += counter_prev[nums[idx] * 2] * counter_after[nums[idx] * 2]

            counter_prev[nums[idx]] += 1
            counter_after[nums[idx + 1]] -= 1

            idx += 1

        return out % (10**9 + 7)
