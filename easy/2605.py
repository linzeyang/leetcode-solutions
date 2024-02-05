"""2605. Form Smallest Number From Two Digit Arrays"""

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        arr1 = [0] * 10
        min1 = min2 = common = 10

        for num in nums1:
            arr1[num] = 1
            if num < min1:
                min1 = num

        for num in nums2:
            if arr1[num] and num < common:
                common = num
            if num < min2:
                min2 = num

        if common < 10:
            return common

        if min1 > min2:
            return min2 * 10 + min1

        return min1 * 10 + min2
