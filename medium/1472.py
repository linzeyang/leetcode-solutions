"""1472. Design Browser History"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self._history = [homepage]
        self._index = 0

    def visit(self, url: str) -> None:
        self._history = self._history[: self._index + 1]
        self._history.append(url)
        self._index += 1

    def back(self, steps: int) -> str:
        steps = min(steps, self._index)
        self._index -= steps

        return self._history[self._index]

    def forward(self, steps: int) -> str:
        steps = min(len(self._history) - self._index - 1, steps)
        self._index += steps

        return self._history[self._index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
