"""1945. Sum of Digits of String After Convert"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = "".join(str(ord(char) - ord("a") + 1) for char in s)

        if len(converted) == 1:
            return int(converted)

        for _ in range(k):
            out = sum(int(char) for char in converted)

            if out < 10:
                return out

            converted = str(out)

        return out
