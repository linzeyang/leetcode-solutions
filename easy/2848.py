"""2848. Points That Intersect With Cars"""

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        out = set()

        for start, end in nums:
            for num in range(start, end + 1):
                out.add(num)

        return len(out)
