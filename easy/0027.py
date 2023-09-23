"""27. Remove Element"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            if nums[left] != val:
                left += 1
                continue

            count += 1

            while left < right:
                if nums[right] == val:
                    count += 1
                    right -= 1
                    continue

                nums[left], nums[right] = nums[right], nums[left]
                break

            left += 1
            right -= 1

        if left == right and nums[left] == val:
            count += 1

        return len(nums) - count
