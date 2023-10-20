"""155. Min Stack"""


class MinStack:
    def __init__(self):
        self._stack: list[int] = []
        self._min_val = None

    def push(self, val: int) -> None:
        self._stack.append(val)

        if self._min_val is None or val < self._min_val:
            self._min_val = val

    def pop(self) -> int:
        val = self._stack.pop()

        if val == self._min_val:
            if not self._stack:
                self._min_val = None
            else:
                self._min_val = min(self._stack)

        return val

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
