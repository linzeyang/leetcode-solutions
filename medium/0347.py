"""347. Top K Frequent Elements"""

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        queue: list[int] = []

        for num, fre in freq.items():
            heapq.heappush(queue, (-fre, num))

        return [heapq.heappop(queue)[1] for _ in range(k)]
