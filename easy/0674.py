"""674. Longest Continuous Increasing Subsequence"""

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        max_count = 0
        count = pointer = 1

        while pointer < len(nums):
            if nums[pointer] > nums[pointer - 1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count

                count = 1

            pointer += 1

        if count > max_count:
            max_count = count

        return max_count
