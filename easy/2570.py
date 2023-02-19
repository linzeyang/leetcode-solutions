"""2570. Merge Two 2D Arrays by Summing Values"""

from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        temp = {lis[0]: lis[1] for lis in nums1}

        for lis in nums2:
            if lis[0] in temp:
                temp[lis[0]] += lis[1]
            else:
                temp[lis[0]] = lis[1]

        return sorted(([key, val] for key, val in temp.items()), key=lambda lis: lis[0])
