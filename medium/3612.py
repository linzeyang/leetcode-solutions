"""3612. Process String with Special Operations I"""


class Solution:
    def processStr(self, s: str) -> str:
        out: list[str] = []

        for char in s:
            if char.isalpha():
                out.append(char)
            elif char == "*":
                if out:
                    out.pop()
            elif char == "#":
                out *= 2
            else:
                out = out[::-1]

        return "".join(out)
