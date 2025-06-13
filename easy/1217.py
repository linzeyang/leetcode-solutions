"""1217. Minimum Cost to Move Chips to The Same Position"""

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        num_of_even = num_of_odd = 0

        for pos in position:
            if pos & 1:
                num_of_odd += 1
            else:
                num_of_even += 1

        return num_of_odd if num_of_even > num_of_odd else num_of_even
