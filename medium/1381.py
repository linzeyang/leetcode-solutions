"""1381. Design a Stack With Increment Operation"""


class CustomStack:
    def __init__(self, maxSize: int):
        self._cap = maxSize
        self._container: list[int] = []

    def push(self, x: int) -> None:
        if len(self._container) >= self._cap:
            return

        self._container.append(x)

    def pop(self) -> int:
        if not self._container:
            return -1

        return self._container.pop()

    def increment(self, k: int, val: int) -> None:
        for idx in range(min(k, len(self._container))):
            self._container[idx] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
