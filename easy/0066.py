"""
66. Plus One
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits

        for i in range(1, len(digits) + 1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] = digits[-i] + 1
                break
        else:
            digits.insert(0, 1)

        return digits
