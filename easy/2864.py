"""2864. Maximum Odd Binary Number"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_of_one = 0

        for char in s:
            if char == "1":
                num_of_one += 1

        if num_of_one == 1:
            return f"{'0' * (len(s) - num_of_one)}1"

        return f"{'1' * (num_of_one - 1)}{'0' * (len(s) - num_of_one)}1"
