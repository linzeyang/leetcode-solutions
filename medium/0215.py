"""215. Kth Largest Element in an Array"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k + 1):
            num = heapq.heappop(nums)

        return num
