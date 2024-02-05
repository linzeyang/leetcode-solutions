"""2670. Find the Distinct Difference Array"""

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        right: dict[int, int] = {}
        out: list[int] = []

        for num in nums:
            if num not in right:
                right[num] = 1
            else:
                right[num] += 1

        left: set[int] = set()

        for num in nums:
            left.add(num)

            if right[num] == 1:
                del right[num]
            else:
                right[num] -= 1

            out.append(len(left) - len(right))

        return out
