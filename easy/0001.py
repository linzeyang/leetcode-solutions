"""1. Two Sum"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if (remaining := target - num) not in mapping:
                mapping[num] = idx
            else:
                return [mapping[remaining], idx]

        return []


def test_solution():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([2, 7, 11, 15], 26) == [2, 3]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
