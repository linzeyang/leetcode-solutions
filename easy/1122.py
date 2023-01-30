"""1122. Relative Sort Array"""

from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cc = Counter(arr1)
        out = []

        for num in arr2:
            for _ in range(cc[num]):
                out.append(num)
            cc.pop(num)

        for num in sorted(cc.keys()):
            for _ in range(cc[num]):
                out.append(num)

        return out
