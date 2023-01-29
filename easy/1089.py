"""1089. Duplicate Zeros"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) == 1:
            return

        i = 0

        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 2
            else:
                i += 1
