"""1286. Iterator for Combination"""

from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self._gen = combinations(characters, combinationLength)
        self._next = None

    def next(self) -> str:
        if self._next is None:
            return "".join(next(self._gen))

        res = self._next
        self._next = None

        return res

    def hasNext(self) -> bool:
        if self._next:
            return True

        try:
            nex = next(self._gen)
        except StopIteration:
            return False

        self._next = "".join(nex)

        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
