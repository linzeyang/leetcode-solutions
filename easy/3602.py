"""3602. Hexadecimal and Hexatrigesimal Conversion"""

from string import ascii_uppercase, digits

HEXATRIGESIMAL_CHART: str = digits + ascii_uppercase


class Solution:
    def concatHex36(self, n: int) -> str:
        part1: str = hex(n**2)[2:].upper()

        cube = n**3

        chars: list[str] = []

        while cube:
            div, mod = divmod(cube, 36)
            chars.append(HEXATRIGESIMAL_CHART[mod])
            cube = div

        part2: str = "".join(reversed(chars))

        return part1 + part2
