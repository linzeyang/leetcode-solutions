"""88. Merge Sorted Array"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(n):
            nums1[m + idx] = nums2[idx]

            for jdx in range(m + idx - 1, -1, -1):
                if nums1[jdx] > nums1[jdx + 1]:
                    nums1[jdx], nums1[jdx + 1] = nums1[jdx + 1], nums1[jdx]
                else:
                    break
