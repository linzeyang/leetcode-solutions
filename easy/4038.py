"""
4038. Count Integers Appearing in a Single Block

https://leetcode.com/problems/count-integers-appearing-in-a-single-block/

Weekly Contest 517
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = [idx]
            elif num == nums[idx - 1]:
                mapping[num][-1] = idx
            else:
                mapping[num].append(idx)

        return sum(1 for val in mapping.values() if len(val) == 1)
