"""645. Set Mismatch"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)

        temp = set()
        dup = -1

        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                dup = num

        return [dup, dup - sum(nums) + (1 + length) * length // 2]
