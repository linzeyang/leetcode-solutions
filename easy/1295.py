"""1295. Find Numbers with Even Number of Digits"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])
