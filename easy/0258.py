"""258. Add Digits"""


class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num = sum(map(int, str(num)))
            if num < 10:
                return num
