"""66. Plus One"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(1, len(digits) + 1):
            if digits[-idx] < 9:
                digits[-idx] += 1
                return digits

            digits[-idx] = 0

        return [1] + digits
