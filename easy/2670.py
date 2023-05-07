"""2670. Find the Distinct Difference Array"""

from collections import Counter
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left = {}
        right = Counter(nums)

        out: list[int] = []

        for num in nums:
            if num not in left:
                left[num] = 1
            else:
                left[num] += 1

            if num in right:
                if right[num] > 1:
                    right[num] -= 1
                else:
                    right.pop(num)

            out.append(len(left) - len(right))

        return out
