"""380. Insert Delete GetRandom O(1)"""

from random import choice


class RandomizedSet:
    def __init__(self):
        self._set = set()
        self._array = []

    def insert(self, val: int) -> bool:
        if val not in self._set:
            self._set.add(val)
            self._array.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        val = choice(self._array)  # noqa: S311

        while val not in self._set:
            val = choice(self._array)  # noqa: S311

        return val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
