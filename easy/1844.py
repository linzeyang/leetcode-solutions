"""1844. Replace All Digits with Characters"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        out = []

        for i in range(0, len(s), 2):
            out.append(s[i])
            if i != len(s) - 1:
                out.append(self.shift(s[i], int(s[i + 1])))

        return "".join(out)

    def shift(self, char: str, n: int) -> str:
        return chr(ord(char) + n)
