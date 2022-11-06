"""1431. Kids With the Greatest Number of Candies"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        base = max(candies) - extraCandies

        return [num >= base for num in candies]
