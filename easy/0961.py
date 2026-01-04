"""961. N-Repeated Element in Size 2N Array"""

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen_nums: set[int] = set()

        for num in nums:
            if num in seen_nums:
                return num

            seen_nums.add(num)
