"""3270. Find the Key of the Numbers"""


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str1 = f"{num1:0>4}"
        str2 = f"{num2:0>4}"
        str3 = f"{num3:0>4}"

        return int(
            "".join(
                [
                    min(str1[0], str2[0], str3[0]),
                    min(str1[1], str2[1], str3[1]),
                    min(str1[2], str2[2], str3[2]),
                    min(str1[3], str2[3], str3[3]),
                ]
            )
        )
