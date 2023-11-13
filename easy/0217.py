"""217. Contains Duplicate"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing: set[int] = set()

        for num in nums:
            if num not in existing:
                existing.add(num)
            else:
                return True

        return False
