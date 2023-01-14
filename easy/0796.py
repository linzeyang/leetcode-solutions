"""796. Rotate String"""

from collections import deque


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        queue1 = deque(s)
        queue2 = deque(goal)

        for _ in range(len(s) - 1):
            queue1.append(queue1.popleft())

            if queue1 == queue2:
                return True

        return False
