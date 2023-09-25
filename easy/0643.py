"""643. Maximum Average Subarray I"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = None
        left = right = summ = 0

        while right < len(nums):
            summ += nums[right]

            if right - left < k - 1:
                right += 1
            else:
                if max_sum is None or summ > max_sum:
                    max_sum = summ

                summ -= nums[left]

                left += 1
                right += 1

        return max_sum / k
