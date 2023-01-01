"""2520. Count the Digits That Divide a Number"""


class Solution:
    def countDigits(self, num: int) -> int:
        out = 0

        for char in str(num):
            if char == "1" or num % int(char) == 0:
                out += 1

        return out
