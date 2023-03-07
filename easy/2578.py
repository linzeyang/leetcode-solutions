"""2578. Split With Minimum Sum"""


class Solution:
    def splitNum(self, num: int) -> int:
        ss = sorted(list(str(num)))

        return int("".join(ss[::2])) + int("".join(ss[1::2]))
