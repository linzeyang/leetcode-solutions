"""3046. Split the Array"""

from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for val in counter.values():
            if val > 2:
                return False

        return True
