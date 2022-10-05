"""476. Number Complement"""


class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** len(f"{num:b}") - 1 - num
