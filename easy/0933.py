"""933. Number of Recent Calls"""


class RecentCounter:
    def __init__(self):
        self._container = []

    def ping(self, t: int) -> int:
        if not self._container:
            self._container.append(t)
            return 1

        self._container.append(t)

        target = t - 3000

        while self._container[0] < target:
            self._container.pop(0)

        return len(self._container)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
