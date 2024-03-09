"""2540. Minimum Common Value"""

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx = jdx = 0

        while idx < len(nums1) and jdx < len(nums2):
            if nums1[idx] == nums2[jdx]:
                return nums1[idx]

            if nums1[idx] < nums2[jdx]:
                idx += 1
            else:
                jdx += 1

        return -1
