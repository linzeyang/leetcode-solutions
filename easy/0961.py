"""961. N-Repeated Element in Size 2N Array"""

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ss = set()

        for num in nums:
            if num in ss:
                return num

            ss.add(num)
