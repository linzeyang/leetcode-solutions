"""1903. Largest Odd Number in String"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx in range(-1, -len(num) - 1, -1):
            if int(num[idx]) % 2 == 1:
                if idx == -1:
                    return num
                return num[: idx + 1]

        return ""
