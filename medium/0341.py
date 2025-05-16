"""341. Flatten Nested List Iterator"""

from copy import copy
from typing import Iterable

from typing_extensions import Self


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer,
        rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds,
        if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list[Self]:
        """
        @return the nested list that this NestedInteger holds,
        if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self._iter_chain: list[Iterable[NestedInteger]] = [iter(nestedList)]

    def next(self) -> int:
        if not self._iter_chain:
            raise StopIteration

        iterr = self._iter_chain[-1]

        try:
            out = next(iterr)
        except StopIteration:
            self._iter_chain.pop(-1)
            return self.next()

        if out.isInteger():
            return out.getInteger()

        self._iter_chain.append(iter(out.getList()))

        return self.next()

    def hasNext(self) -> bool:
        if not self._iter_chain:
            return False

        iterr = self._iter_chain[-1]

        cp_iter = copy(iterr)

        try:
            nex = next(cp_iter)
        except StopIteration:
            self._iter_chain.pop(-1)
            return self.hasNext()

        if nex.isInteger():
            return True

        nex = next(iterr)

        self._iter_chain.append(iter(nex.getList()))

        return self.hasNext()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
