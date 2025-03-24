"""8. String to Integer (atoi)"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        signed = False
        temp = []

        ll = len(s)

        for i in range(ll):
            c = s[i]
            if c == " ":
                if signed:
                    break
                if not temp:
                    continue
                break
            if c == "-":
                if signed:
                    break
                if not temp:
                    sign = -1
                    signed = True
                    continue
                break
            if c == "+":
                if signed:
                    break
                if not temp:
                    signed = True
                    continue
                break
            if "0" <= c <= "9":
                temp.append(int(c))
            elif not temp:
                return 0
            else:
                break

        if not temp:
            return 0

        result = 0

        for i in range(1, len(temp) + 1):
            result += temp[-i] * (10 ** (i - 1))

        result *= sign

        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -(2**31):
            return -(2**31)

        return result
