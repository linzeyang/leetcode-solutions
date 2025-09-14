"""3684. Maximize Sum of At Most K Distinct Elements"""

from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums_unique_sorted: list[int] = sorted(set(nums), reverse=True)

        return nums_unique_sorted[:k]
