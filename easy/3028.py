"""3028. Ant on the Boundary"""

from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = out = 0

        for num in nums:
            pos += num

            if not pos:
                out += 1

        return out
