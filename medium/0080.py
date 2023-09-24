"""80. Remove Duplicates from Sorted Array II"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = count = 0

        while fast < len(nums) - count:
            if nums[fast] != nums[slow]:
                slow = fast
                continue

            if fast - slow >= 2:
                count += 1

                for idx in range(fast, len(nums) - 1):
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
            else:
                fast += 1

        return fast
