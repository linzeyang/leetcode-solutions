"""1725. Number Of Rectangles That Can Form The Largest Square"""

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        maxx = 0

        for x, y in rectangles:
            length = min(x, y)

            if length > maxx:
                maxx = length
                count = 1
            elif length == maxx:
                count += 1

        return count
