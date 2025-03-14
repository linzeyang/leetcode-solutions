"""3379. Transformed Array"""

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        return [nums[(idx + num) % length] for idx, num in enumerate(nums)]
