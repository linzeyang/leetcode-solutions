"""2190. Most Frequent Number Following Key In an Array"""

from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        temp = {}

        for idx in range(1, len(nums)):
            if nums[idx - 1] == key:
                if nums[idx] not in temp:
                    temp[nums[idx]] = 1
                else:
                    temp[nums[idx]] += 1

        maxx = max(temp.values())

        return next(num for num, count in temp.items() if count == maxx)
