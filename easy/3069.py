"""
3069. Distribute Elements Into Two Arrays I

https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

Weekly Contest 387
"""

from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1: list[int] = [nums[0]]
        arr2: list[int] = [nums[1]]

        for idx in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[idx])
            else:
                arr2.append(nums[idx])

        return arr1 + arr2
