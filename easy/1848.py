"""1848. Minimum Distance to the Target Element"""

from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if len(nums) == 1 or nums[start] == target:
            return 0

        distance_to_edge = max(len(nums) - start, start + 1)

        for i in range(1, distance_to_edge):
            if ((start - i) >= 0 and nums[start - i] == target) or (
                (start + i) < len(nums) and nums[start + i] == target
            ):
                return i
