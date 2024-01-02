"""2610. Convert an Array Into a 2D Array With Conditions"""

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mapping: dict[int, int] = {}

        out: list[list[int]] = []

        for num in nums:
            if num not in mapping:
                count = 1
            else:
                count = mapping[num] + 1

            mapping[num] = count

            if len(out) < count:
                out.append([num])
            else:
                out[count - 1].append(num)

        return out
