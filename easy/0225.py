"""
225. Implement Stack using Queues
"""

from collections import deque


# Runtime: 50 ms, faster than 46.61% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14 MB, less than 25.81% of Python3 online submissions for Implement Stack using Queues.
class MyStack:
    def __init__(self):
        self._main_queue = deque()
        self._back_queue = deque()

    def push(self, x: int) -> None:
        if self._main_queue:
            self._back_queue.append(self._main_queue.popleft())

        self._main_queue.append(x)

        for _ in range(len(self._back_queue) - 1):
            self._back_queue.append(self._back_queue.popleft())

    def pop(self) -> int:
        val = self._main_queue.popleft()

        if self._back_queue:
            self._main_queue.append(self._back_queue.popleft())

        return val

    def top(self) -> int:
        return self._main_queue[0]

    def empty(self) -> bool:
        return not self._main_queue and not self._back_queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
