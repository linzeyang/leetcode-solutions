"""1352. Product of the Last K Numbers"""


class ProductOfNumbers:

    def __init__(self):
        self._prefix_prods: list[int] = []

    def add(self, num: int) -> None:
        if num == 0:
            self._prefix_prods = []
        elif not self._prefix_prods:
            self._prefix_prods.append(num)
        else:
            self._prefix_prods.append(num * self._prefix_prods[-1])

    def getProduct(self, k: int) -> int:
        if k > len(self._prefix_prods):
            return 0

        if k == len(self._prefix_prods):
            return self._prefix_prods[-1]

        return self._prefix_prods[-1] // self._prefix_prods[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
