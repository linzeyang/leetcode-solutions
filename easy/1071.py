"""1071. Greatest Common Divisor of Strings"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        common = self._gcd(len1, len2)
        common_str = str1[:common]

        if (
            common_str * (len1 // common) == str1
            and common_str * (len2 // common) == str2
        ):
            return common_str

        return ""

    def _gcd(self, num1: int, num2: int) -> int:
        if num1 < num2:
            num1, num2 = num2, num1

        while num1 % num2 != 0:
            num1, num2 = num2, num1 - num2

            if num1 < num2:
                num1, num2 = num2, num1

        return num2
