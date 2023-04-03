"""2605. Form Smallest Number From Two Digit Arrays"""

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if inter := set(nums1) & set(nums2):
            return min(inter)

        num_a = min(nums1)
        num_b = min(nums2)

        if num_a < num_b:
            return num_a * 10 + num_b
        return num_b * 10 + num_a
