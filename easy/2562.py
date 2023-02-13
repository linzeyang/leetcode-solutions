"""2562. Find the Array Concatenation Value"""

from collections import deque
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        queue = deque(nums)
        out = 0

        while len(queue) > 1:
            num_a = queue.popleft()
            num_b = queue.pop()

            out += int(f"{num_a}{num_b}")

        if queue:
            out += queue[0]

        return out
