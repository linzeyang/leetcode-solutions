"""2956. Find Common Elements Between Two Arrays"""

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [
            sum(1 for num in nums1 if num in set(nums2)),
            sum(1 for num in nums2 if num in set(nums1)),
        ]
