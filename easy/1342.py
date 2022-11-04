"""1342. Number of Steps to Reduce a Number to Zero"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1

        return count
