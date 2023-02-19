"""2566. Maximum Difference by Remapping a Digit"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        leading = str_num[0]

        for char in str_num:
            if char != "9":
                non_nine = char
                break
        else:
            non_nine = "9"

        return int(str_num.replace(non_nine, "9")) - int(str_num.replace(leading, "0"))
