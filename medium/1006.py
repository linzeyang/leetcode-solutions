"""1006. Clumsy Factorial"""

from itertools import cycle


class Solution:
    def clumsy(self, n: int) -> int:
        temp = []

        for num, oper in zip(range(n, 0, -1), cycle(("*", "//", "+", "-"))):
            temp.append(str(num))
            temp.append(oper)

        temp.pop()

        return eval("".join(temp))
