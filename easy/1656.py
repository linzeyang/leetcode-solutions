"""1656. Design an Ordered Stream"""

from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self._slots: list[str | None] = [None] * n
        self._idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idx = idKey - 1
        self._slots[idx] = value

        if self._idx != idx:
            return []

        while self._idx < len(self._slots):
            if self._slots[self._idx] is None:
                break

            self._idx += 1

        return self._slots[idx : self._idx]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
