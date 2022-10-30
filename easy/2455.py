"""2455. Average Value of Even Numbers That Are Divisible by Three"""

from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ll = [num for num in nums if num % 6 == 0]

        if not ll:
            return 0

        return sum(ll) // len(ll)
