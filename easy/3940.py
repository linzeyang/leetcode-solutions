"""
3940. Limit Occurrences in Sorted Array

https://leetcode.com/problems/limit-occurrences-in-sorted-array/

Weekly Contest 503
"""


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        out: list[int] = [nums[0]]

        current: int = nums[0]
        freq: int = 1

        for idx in range(1, len(nums)):
            num: int = nums[idx]

            if num == current:
                freq += 1
                if freq <= k:
                    out.append(num)
            else:
                current = num
                freq = 1
                out.append(num)

        return out
