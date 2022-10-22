"""2206. Divide Array Into Equal Pairs"""

from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cc = Counter(nums)

        for val in cc.values():
            if val % 2 != 0:
                return False

        return True
