"""3158. Find the XOR of Numbers Which Appear Twice"""

from functools import reduce
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        exists: set[int] = set()
        dups: set[int] = set()

        for num in nums:
            if num not in exists:
                exists.add(num)
            else:
                dups.add(num)

        if not dups:
            return 0

        return reduce(lambda x, y: x ^ y, dups)
