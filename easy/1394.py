"""1394. Find Lucky Integer in an Array"""

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cc = Counter(arr)

        return max((k for k, v in cc.items() if k == v), default=-1)
