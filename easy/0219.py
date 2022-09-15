"""
219. Contains Duplicate II
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Slow:
        # Runtime: 1280 ms, faster than 21.68% of Python3 online submissions for Contains Duplicate II.
        # Memory Usage: 27.4 MB, less than 30.48% of Python3 online submissions for Contains Duplicate II.
        if (length := len(nums)) < 2:
            return False

        temp = {}

        for i in range(length):
            if (n := nums[i]) not in temp:
                temp[n] = i
            elif i - temp[n] > k:
                temp[n] = i
            else:
                return True

        return False
