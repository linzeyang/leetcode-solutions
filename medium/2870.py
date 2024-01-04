"""2870. Minimum Number of Operations to Make Array Empty"""

from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cc = Counter(nums)
        out = 0

        for count in cc.values():
            if count < 2:
                return -1

            if count % 3 == 0:
                out += count // 3
            elif count % 3 == 2:
                out += count // 3 + 1
            else:
                out += (count - 4) // 3 + 2

        return out
