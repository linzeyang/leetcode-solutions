"""492. Construct the Rectangle"""

from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = int(area**0.5)

        for num in range(sqrt, 0, -1):
            if area % num == 0:
                return [area // num, num]

        return []  # only for type-checking
