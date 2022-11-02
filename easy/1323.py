"""1323. Maximum 69 Number"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        out = []
        found = 0

        for char in str(num):
            if char == "9":
                out.append(char)
            elif char == "6" and not found:
                out.append("9")
                found = 1
            else:
                out.append("6")

        return int("".join(out))
