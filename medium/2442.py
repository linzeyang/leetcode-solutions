"""2442. Count Number of Distinct Integers After Reverse Operations"""

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)

        for idx in range(length):
            nums.append(int(str(nums[idx])[::-1]))

        return len(set(nums))
