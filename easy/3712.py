"""3712. Sum of Elements With Frequency Divisible by K"""

from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter: Counter[int] = Counter(nums)

        out: int = 0

        for num, freq in counter.items():
            if freq % k == 0:
                out += num * freq

        return out
