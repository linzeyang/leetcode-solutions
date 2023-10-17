"""260. Single Number III"""

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)

        return [num for num, count in cc.items() if count == 1]
