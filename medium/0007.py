"""7. Reverse Integer"""


class Solution:
    def reverse(self, x: int) -> int:
        if -9 <= x <= 9:
            return x

        temp = []

        a = abs(x)

        while a >= 10:
            temp.append(a % 10)
            a = int(a / 10)

        temp.append(a)

        result = 0

        for i in range(len(temp)):
            result += temp[i] * (10 ** (len(temp) - i - 1))

        if result > 2**31 - 1:
            return 0

        return result if x >= 0 else -result
