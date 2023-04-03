"""2610. Convert an Array Into a 2D Array With Conditions"""

from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        out: list[list[int]] = []

        cc = Counter(nums)

        while cc:
            temp = []

            for k, v in list(cc.items()):
                temp.append(k)
                cc[k] = v - 1

                if v == 1:
                    cc.pop(k)

            out.append(temp)

        return out
