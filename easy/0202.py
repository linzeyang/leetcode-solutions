"""202. Happy Number"""


class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()

        while True:
            t = calc(n)

            if t == 1:
                return True

            if t in temp:
                return False

            temp.add(t)
            n = t


def calc(num: int) -> int:
    return sum(int(char) ** 2 for char in str(num))
