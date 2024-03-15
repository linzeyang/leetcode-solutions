"""3074. Apple Redistribution into Boxes"""

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)

        capacity.sort(reverse=True)

        sub_capacity = 0

        for idx, cap in enumerate(capacity):
            sub_capacity += cap

            if sub_capacity >= total_apple:
                return idx + 1

        return -1
