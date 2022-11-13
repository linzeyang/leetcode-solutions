"""1403. Minimum Subsequence in Non-Increasing Order"""


from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        half = sum(nums) / 2

        out = []
        summ = 0

        for num in sorted(nums, reverse=True):
            out.append(num)
            summ += num
            if summ > half:
                return out
