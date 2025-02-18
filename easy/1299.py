"""1299. Replace Elements with Greatest Element on Right Side"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1

        for idx in range(1, len(arr) + 1):
            current = arr[-idx]
            arr[-idx] = current_max

            current_max = max(current_max, current)

        return arr
