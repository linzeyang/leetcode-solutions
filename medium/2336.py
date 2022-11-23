"""2336. Smallest Number in Infinite Set"""


class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self._resting = set()

    def popSmallest(self) -> int:
        if not self._resting:
            cur = self.current
            self.current += 1
            return cur

        num = min(self._resting)
        self._resting.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num < self.current:
            self._resting.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
