"""3005. Count Elements With Maximum Frequency"""

from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter: Counter[int] = Counter(nums)

        max_freq: int = max(counter.values())

        out: int = 0

        for freq in counter.values():
            if freq == max_freq:
                out += freq

        return out
