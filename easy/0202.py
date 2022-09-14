"""
202. Happy Number
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        # Very slow:
        # Runtime: 72 ms, faster than 14.61% of Python3 online submissions for Happy Number.
        # Memory Usage: 13.9 MB, less than 61.72% of Python3 online submissions for Happy Number.
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
