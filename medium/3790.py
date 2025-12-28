"""3790. Smallest All-Ones Multiple"""


class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        num: int = 1
        out = 1
        mods: set[int] = set()

        while True:
            if (mod := num % k) == 0:
                return out

            if mod in mods:
                return -1

            num = mod * 10 + 1
            out += 1
            mods.add(mod)
