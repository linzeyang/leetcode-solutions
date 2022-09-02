"""
4. Median of Two Sorted Arrays
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)

        if total == 0:
            return float(0)
        if total == 1:
            return (nums1 + nums2)[0]

        temp = []

        count = 0

        a = b = 0

        while count < (int(total / 2) + 1):
            if a == len(nums1) and b == len(nums2):
                break
            if a == len(nums1):
                temp.append(nums2[b])
                b += 1
            elif b == len(nums2):
                temp.append(nums1[a])
                a += 1
            elif nums1[a] < nums2[b]:
                temp.append(nums1[a])
                a += 1
            else:
                temp.append(nums2[b])
                b += 1
            count += 1

        if total % 2 == 0:
            return (temp[-1] + temp[-2]) / 2
        else:
            return temp[-1]
