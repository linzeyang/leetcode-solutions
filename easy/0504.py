"""504. Base 7"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = 1 if num > 0 else -1

        digits: list[str] = []

        num = abs(num)

        while num:
            div, mod = divmod(num, 7)
            digits.append(str(mod))
            num = div

        return ("" if sign > 0 else "-") + "".join(reversed(digits))
