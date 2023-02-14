"""1893. Check if All the Integers in a Range Are Covered"""

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            for ran in ranges:
                if ran[0] <= num <= ran[1]:
                    break
            else:
                return False

        return True
