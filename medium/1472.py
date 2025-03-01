"""1472. Design Browser History"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self._history: list[str] = [homepage]
        self._current_idx: int = 0

    def visit(self, url: str) -> None:
        for _ in range(len(self._history) - self._current_idx - 1):
            self._history.pop()

        self._history.append(url)
        self._current_idx += 1

    def back(self, steps: int) -> str:
        self._current_idx = max(self._current_idx - steps, 0)

        return self._history[self._current_idx]

    def forward(self, steps: int) -> str:
        self._current_idx = min(self._current_idx + steps, len(self._history) - 1)

        return self._history[self._current_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
