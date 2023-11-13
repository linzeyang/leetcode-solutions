"""219. Contains Duplicate II"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        existing: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if num not in existing or idx - existing[num] > k:
                existing[num] = idx
            else:
                return True

        return False
