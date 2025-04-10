"""3038. Maximum Number of Operations With the Same Score I"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        nums = nums[::-1]

        target = nums.pop() + nums.pop()

        out = 1

        while len(nums) >= 2:
            current = nums.pop() + nums.pop()

            if current != target:
                break

            out += 1

        return out
