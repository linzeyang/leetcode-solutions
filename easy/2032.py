"""2032. Two Out of Three"""

from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        out = set()

        for n in s1:
            if n in s2:
                out.add(n)
                s2.remove(n)
            if n in s3:
                out.add(n)
                s3.remove(n)

        for n in s2:
            if n in s3:
                out.add(n)

        return list(out)
