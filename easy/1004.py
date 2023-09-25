"""1004. Max Consecutive Ones III"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = num_of_zero = max_count = 0

        while right < len(nums):
            if not nums[right]:
                if num_of_zero == k:
                    count = right - left

                    if count > max_count:
                        max_count = count

                    while num_of_zero == k:
                        if not nums[left]:
                            num_of_zero -= 1
                        left += 1
                else:
                    num_of_zero += 1
                    right += 1
            else:
                right += 1

        if not max_count and num_of_zero:
            return len(nums)

        if right - left > max_count:
            max_count = right - left

        return max_count
