"""
405. Convert a Number to Hexadecimal
"""


class Solution:
    def toHex(self, num: int) -> str:
        # Runtime: 57 ms, faster than 26.04% of Python3 online submissions for Convert a Number to Hexadecimal.
        # Memory Usage: 13.8 MB, less than 96.98% of Python3 online submissions for Convert a Number to Hexadecimal.
        if num == 0:
            return "0"

        if num > 0:
            ll = get_positive(num)
        else:
            ll = get_positive(num * (-1) - 1)
            ll += [0] * (8 - len(ll))
            ll = [(15 - n) for n in ll]

        return "".join(MAPPING.get(num, str(num)) for num in ll[::-1])


MAPPING = {
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


def get_positive(num: int) -> list[int]:
    if num == 0:
        return [0]

    out = []

    while num > 0:
        out.append(num % 16)
        num //= 16

    return out
