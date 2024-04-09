"""3099. Harshad Number"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = sum(int(char) for char in str(x))

        return sum_of_digits if x % sum_of_digits == 0 else -1
