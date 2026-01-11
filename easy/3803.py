"""3803. Count Residue Prefixes"""


class Solution:
    def residuePrefixes(self, s: str) -> int:
        out: int = 0

        char_set: set[str] = set()

        for idx, char in enumerate(s, start=1):
            char_set.add(char)

            if len(char_set) == idx % 3:
                out += 1

        return out
