"""3769. Sort Integers by Binary Reflection"""

from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def get_reflection(num: int) -> int:
            # Convert to binary, remove '0b', reverse, and parse as base 2
            return int(bin(num)[2:][::-1], base=2)

        # Sort by reflection value first, then by the number itself
        return sorted(nums, key=lambda x: (get_reflection(num=x), x))
