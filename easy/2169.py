"""2169. Count Operations to Obtain Zero"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if not num1 or not num2:
            return 0

        if num1 < num2:
            num1, num2 = num2, num1

        return num1 // num2 + self.countOperations(num1 % num2, num2)
