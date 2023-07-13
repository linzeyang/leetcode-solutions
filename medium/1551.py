"""1551. Minimum Operations to Make Array Equal"""


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2:
            return (n // 2) * (n // 2 + 1)

        return (n // 2) ** 2
