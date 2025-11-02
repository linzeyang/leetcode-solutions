"""3731. Find Missing Elements"""

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        existing: set[int] = set(nums)

        min_num: int = min(nums)
        max_num: int = max(nums)

        if max_num - min_num + 1 == len(existing):
            return []

        return [num for num in range(min_num + 1, max_num) if num not in existing]
