"""3066. Minimum Operations to Exceed Threshold Value II"""

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = 0

        heapq.heapify(nums)

        num1 = heapq.heappop(nums)

        while num1 < k:
            num2 = heapq.heappop(nums)

            heapq.heappush(nums, min(num1, num2) * 2 + max(num1, num2))

            out += 1

            num1 = heapq.heappop(nums)

        return out
