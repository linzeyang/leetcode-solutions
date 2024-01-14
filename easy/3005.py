"""3005. Count Elements With Maximum Frequency"""

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        top_freq = 0
        top_freq_count = 0

        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

            if counter[num] > top_freq:
                top_freq = counter[num]
                top_freq_count = 1
            elif counter[num] == top_freq:
                top_freq_count += 1

        return top_freq * top_freq_count
