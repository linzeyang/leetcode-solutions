"""1005. Maximize Sum Of Array After K Negations"""

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        minn = min(nums)

        if minn >= 0:
            if k % 2 == 0:
                return sum(nums)

            return sum(nums) - 2 * minn

        nums = sorted(nums)

        for idx, num in enumerate(nums):
            if num < 0 and k > 0:
                nums[idx] = -nums[idx]
                k -= 1
            else:
                break

        if k == 0 or k % 2 == 0:
            return sum(nums)

        if nums[idx] == 0:
            return sum(nums)

        if idx + 1 < len(nums):
            return sum(nums) - 2 * min(
                abs(nums[idx - 1]), abs(nums[idx]), abs(nums[idx + 1])
            )

        return sum(nums) - 2 * min(abs(nums[idx - 1]), abs(nums[idx]))
