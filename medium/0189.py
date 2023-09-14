"""189. Rotate Array"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        for idx in range(len(nums) // 2):
            nums[idx], nums[-idx - 1] = nums[-idx - 1], nums[idx]

        print(nums)

        for idx in range(k // 2):
            nums[idx], nums[k - idx - 1] = nums[k - idx - 1], nums[idx]

        print(nums)

        for idx in range(k, (len(nums) + k) // 2):
            nums[idx], nums[k - idx - 1] = nums[k - idx - 1], nums[idx]
