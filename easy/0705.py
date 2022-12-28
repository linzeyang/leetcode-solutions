"""705. Design HashSet"""


class MyHashSet:
    def __init__(self):
        self._capacity = 100
        self._slots = [[]] * self._capacity

    def _index(self, key: int) -> int:
        return key % self._capacity

    def add(self, key: int) -> None:
        idx = self._index(key)

        if key not in self._slots[idx]:
            self._slots[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._index(key)

        if key in self._slots[idx]:
            self._slots[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._index(key)

        return key in self._slots[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
