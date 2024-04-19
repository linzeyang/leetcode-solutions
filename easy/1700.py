"""1700. Number of Students Unable to Eat Lunch"""

from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = sandwiches[::-1]
        size = len(students)
        num_pass = 0

        while stack:
            if queue[0] == stack[-1]:
                queue.popleft()
                stack.pop()
                num_pass = 0
            else:
                queue.append(queue.popleft())
                num_pass += 1

                if num_pass >= size:
                    return len(queue)

        return 0
