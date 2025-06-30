"""594. Longest Harmonious Subsequence"""

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter: Counter[int] = Counter(nums)
        keys_sorted: list[int] = sorted(counter.keys())

        out = 0

        for idx in range(len(keys_sorted) - 1):
            if (num1 := keys_sorted[idx]) - (num2 := keys_sorted[idx + 1]) == -1:
                out = max(out, counter[num1] + counter[num2])

        return out
