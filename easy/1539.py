"""1539. Kth Missing Positive Number"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        existing: set[int] = set(arr)

        num = 1
        counter = 0

        while counter < k:
            if num not in existing:
                counter += 1
            num += 1

        return num - 1
