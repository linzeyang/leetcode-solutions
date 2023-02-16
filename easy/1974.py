"""1974. Minimum Time to Type Word Using Special Typewriter"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        out = 0
        pointer = ord("a")

        for char in word:
            offset = ord(char) - pointer

            if offset < 0:
                offset = -offset

            if offset > 13:
                out += 26 - offset
            else:
                out += offset

            out += 1
            pointer = ord(char)

        return out
