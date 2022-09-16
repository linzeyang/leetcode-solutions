"""
349. Intersection of Two Arrays
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Slow:
        # Runtime: 99 ms, faster than 24.76% of Python3 online submissions for Intersection of Two Arrays.
        # Memory Usage: 14.2 MB, less than 24.99% of Python3 online submissions for Intersection of Two Arrays.
        return list(set(nums1) & set(nums2))
