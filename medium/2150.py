"""2150. Find All Lonely Numbers in the Array"""

from collections import Counter
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)
        out = []

        for num, count in cc.items():
            if count > 1:
                continue

            if num + 1 not in cc and num - 1 not in cc:
                out.append(num)

        return out
