"""1637. Widest Vertical Area Between Two Points Containing No Points"""

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lis = sorted(point[0] for point in points)

        return max(lis[idx] - lis[idx - 1] for idx in range(1, len(lis)))
