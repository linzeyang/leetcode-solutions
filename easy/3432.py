"""3432. Count Partitions with Even Sum Difference"""

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (len(nums) - 1) if sum(nums) & 1 == 0 else 0
