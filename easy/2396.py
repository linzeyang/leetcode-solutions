"""2395. Find Subarrays With Equal Sum"""

from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if (length := len(nums)) < 3:
            return False

        temp = set()

        for idx in range(length - 1):
            if (summ := nums[idx] + nums[idx + 1]) not in temp:
                temp.add(summ)
            else:
                return True

        return False
