"""2180. Count Integers With Even Digit Sum"""


class Solution:
    def countEven(self, num: int) -> int:
        if num < 10:
            return num // 2

        num_of_twenties = num // 20

        out = num_of_twenties * 10 - 1

        for nu in range(num_of_twenties * 20 + 1, num + 1):
            if sum(int(char) for char in str(nu)) % 2 == 0:
                out += 1

        return out
