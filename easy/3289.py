"""3289. The Two Sneaky Numbers of Digitville"""

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        out: list[int] = []
        temp: set[int] = set()

        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                out.append(num)
                temp.remove(num)

        return out
