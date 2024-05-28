"""3162. Find the Number of Good Pairs I"""

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(1 for numx in nums1 for numy in nums2 if numx % (numy * k) == 0)
