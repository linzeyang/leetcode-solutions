"""706. Design HashMap"""


class MyHashMap:
    def __init__(self):
        self._capacity = 100
        self._container = [[]] * self._capacity

    def _index(self, key):
        return hash(key) % self._capacity

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)

        for i, (k, _) in enumerate(self._container[idx]):
            if key == k:
                self._container[idx][i] = key, value
                break
        else:
            self._container[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._index(key)

        for k, v in self._container[idx]:
            if key == k:
                return v

        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)

        for i, (k, _) in enumerate(self._container[idx]):
            if key == k:
                self._container[idx].pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
