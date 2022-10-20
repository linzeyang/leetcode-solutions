"""2427. Number of Common Factors"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 1
        i = 2

        while i <= min(a, b):
            if a % i == 0 and b % i == 0:
                count += 1
            i += 1

        return count
