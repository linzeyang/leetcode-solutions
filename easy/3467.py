"""3467. Transform Array by Parity"""

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        num_even = num_odd = 0

        for num in nums:
            if num & 1:
                num_odd += 1
            else:
                num_even += 1

        return [0] * num_even + [1] * num_odd
