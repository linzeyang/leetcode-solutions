"""1460. Make Two Arrays Equal by Reversing Subarrays"""

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
