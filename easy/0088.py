"""88. Merge Sorted Array"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Runtime: 71 ms, faster than 34.88% of Python3 online submissions for Merge Sorted Array.
        # Memory Usage: 13.9 MB, less than 85.55% of Python3 online submissions for Merge Sorted Array.
        if m == 0:
            for j in range(n):
                nums1[j] = nums2[j]
            return

        i = 0

        for j, num in enumerate(nums2):
            while i < m + n:
                if num <= nums1[i]:
                    nums1.insert(i, num)
                    nums1.pop()
                    i += 1
                    break
                if nums1[i] == 0 and i >= m + j:
                    nums1[i] = num
                    i += 1
                    break
                i += 1
