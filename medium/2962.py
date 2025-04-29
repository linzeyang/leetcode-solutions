"""2962. Count Subarrays Where Max Element Appears at Least K Times"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)

        length = len(nums)

        out = counter = left = right = 0

        while right < length:
            if nums[right] == target:
                counter += 1

            while counter >= k:
                out += length - right

                if nums[left] == target:
                    counter -= 1

                left += 1

            right += 1

        return out
