"""2549. Count Distinct Numbers on Board"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1
