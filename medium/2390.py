"""2390. Removing Stars From a String"""


class Solution:
    def removeStars(self, s: str) -> str:
        out: list[str] = []

        for char in s:
            if char == "*":
                out.pop()
            else:
                out.append(char)

        return "".join(out)
