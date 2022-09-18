"""
232. Implement Queue using Stacks
"""


# Runtime: 56 ms, faster than 29.01% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 14 MB, less than 75.28% of Python3 online submissions for Implement Queue using Stacks.
class MyQueue:
    def __init__(self):
        self._main_stack = []
        self._back_stack = []

    def push(self, x: int) -> None:
        if not self._main_stack:
            self._main_stack.append(x)
        else:
            size = len(self._back_stack)

            for _ in range(size):
                self._main_stack.append(self._back_stack.pop())

            self._back_stack.append(x)

            for _ in range(size):
                self._back_stack.append(self._main_stack.pop())

    def pop(self) -> int:
        val = self._main_stack.pop()

        if self._back_stack:
            self._main_stack.append(self._back_stack.pop())

        return val

    def peek(self) -> int:
        return self._main_stack[-1]

    def empty(self) -> bool:
        return not self._main_stack and not self._back_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
