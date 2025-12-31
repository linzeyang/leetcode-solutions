"""3693. Climbing Stairs II"""

from collections import deque
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        queue: deque[int] = deque([0, costs[0] + 1])

        if len(costs) < 2:
            return queue[-1]

        queue.append(min(queue[-1] + costs[1] + 1, costs[1] + 4))

        for idx in range(2, len(costs)):
            queue.append(
                min(
                    queue[-1] + costs[idx] + 1,
                    queue[-2] + costs[idx] + 4,
                    queue[-3] + costs[idx] + 9,
                )
            )
            queue.popleft()

        return queue[-1]
