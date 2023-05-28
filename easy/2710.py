"""2710. Remove Trailing Zeros From a String"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # one-line solution:
        # return num.rstrip("0")

        for idx in range(1, len(num) + 1):
            if num[-idx] != "0":
                return num[: len(num) - idx + 1]
        return ""
