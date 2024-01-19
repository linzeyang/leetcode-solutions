"""350. Intersection of Two Arrays II"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        dic2 = {}

        for num in nums1:
            if num not in dic1:
                dic1[num] = 1
            else:
                dic1[num] += 1

        for num in nums2:
            if num not in dic2:
                dic2[num] = 1
            else:
                dic2[num] += 1

        out = []

        for num in set(dic1.keys()) & set(dic2.keys()):
            out.extend([num] * min(dic1[num], dic2[num]))

        return out
