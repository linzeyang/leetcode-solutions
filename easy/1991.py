"""1991. Find the Middle Index in Array"""

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l_sum = 0
        total = sum(nums)

        for idx, num in enumerate(nums):
            if (total - num) % 2:
                l_sum += num
                continue

            if l_sum == (total - num) // 2:
                return idx

            l_sum += num

        return -1
