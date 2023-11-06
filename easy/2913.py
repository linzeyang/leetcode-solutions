"""2913. Subarrays Distinct Element Sum of Squares I"""

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0

        for idx, num in enumerate(nums):
            sett = {num}
            count += 1

            for _ in range(len(nums) - idx - 1):
                sett.add(nums[idx + _ + 1])
                count += len(sett) ** 2

        if count > 1e9 + 7:
            return count % (int(1e9) + 7)

        return count
