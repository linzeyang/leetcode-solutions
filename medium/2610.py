"""2610. Convert an Array Into a 2D Array With Conditions"""

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        out: list[list[int]] = [[]]

        for num in nums:
            for row in out:
                if num not in row:
                    row.append(num)
                    break
            else:
                out.append([num])

        return out
