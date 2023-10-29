"""225. Implement Stack using Queues"""

from queue import Queue


class MyStack:
    def __init__(self):
        self.inner_queue = Queue()
        self.outer_queue = Queue()

    def push(self, x: int) -> None:
        if not self.outer_queue.empty():
            num = self.outer_queue.get()
            self.inner_queue.put(num)

        self.outer_queue.put(x)

    def pop(self) -> int:
        num = self.outer_queue.get()

        if not self.inner_queue.empty():
            for _ in range(self.inner_queue.qsize() - 1):
                inner = self.inner_queue.get()
                self.inner_queue.put(inner)

            self.outer_queue.put(self.inner_queue.get())

        return num

    def top(self) -> int:
        num = self.outer_queue.get()
        self.outer_queue.put(num)

        return num

    def empty(self) -> bool:
        return self.inner_queue.empty() and self.outer_queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
