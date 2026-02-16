"""3843. First Element with Unique Frequency"""

from collections import Counter
from typing import List


class Solution:
    """
    https://leetcode.com/problems/first-element-with-unique-frequency/
    Weekly Contest 489
    """

    def firstUniqueFreq(self, nums: List[int]) -> int:
        counter1: Counter[int] = Counter(nums)
        counter2: Counter[int] = Counter(counter1.values())

        unique_freqs: set[int] = {
            freq for freq, count in counter2.items() if count == 1
        }

        if not unique_freqs:
            return -1

        for num, freq in counter1.items():
            if freq in unique_freqs:
                return num

        return -1
