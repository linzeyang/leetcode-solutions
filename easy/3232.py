"""3232. Find if Digit Game Can Be Won"""

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_less_than_ten = sum_otherwise = 0

        for num in nums:
            if num < 10:
                sum_less_than_ten += num
            else:
                sum_otherwise += num

        return sum_less_than_ten != sum_otherwise
