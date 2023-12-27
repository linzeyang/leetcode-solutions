"""2427. Number of Common Factors"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        oria, orib = a, b

        while b:
            a, b = b, a % b

        if a == 1:
            return 1

        out = 2

        for num in range(2, a):
            if not oria % num and not orib % num:
                out += 1

        return out
