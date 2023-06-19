"""442. Find All Duplicates in an Array"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp = set()
        out = []

        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                out.append(num)

        return out
