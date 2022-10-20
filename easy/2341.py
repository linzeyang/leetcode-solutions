"""2341. Maximum Number of Pairs in Array"""

from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        a, b = 0, 0

        for v in c.values():
            x, y = divmod(v, 2)
            a += x
            b += y

        return [a, b]
