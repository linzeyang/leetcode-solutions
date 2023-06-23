"""2161. Partition Array According to Given Pivot"""

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        mid = []

        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                after.append(num)

        return before + mid + after
