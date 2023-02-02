"""1287. Element Appearing More Than 25% In Sorted Array"""

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        freq = len(arr) // 4

        count = 0
        target = -1

        for num in arr:
            if num == target:
                count += 1
            else:
                target = num
                count = 1

            if count > freq:
                return target
