"""2465. Number of Distinct Averages"""

from collections import deque
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        deq = deque(sorted(nums))
        ss = set()

        while deq:
            a = deq.popleft()
            b = deq.pop()
            ss.add((a + b) / 2)

        return len(ss)
