"""
67. Add Binary
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Using python built-in functions:
        # return bin(int(a, 2) + int(b, 2))[2:]

        if (la := len(a)) > (lb := len(b)):
            a, b = b, a
            la, lb = lb, la

        out = []

        adv = "0"

        for i in range(1, lb + 1):
            nb = b[-i]

            if i > la:
                na = "0"
            else:
                na = a[-i]

            if (na, nb) == ("0", "0"):
                out.append(adv)
                adv = "0"
            elif (na, nb) in (
                ("0", "1"),
                ("1", "0"),
            ):
                if adv == "0":
                    out.append("1")
                else:
                    out.append("0")
            else:
                out.append(adv)
                adv = "1"

        if adv == "1":
            out.append("1")

        return "".join(out[::-1])
