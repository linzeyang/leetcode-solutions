"""3560. Find Minimum Log Transportation Cost"""


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return max(m - k, 0) * k + max(n - k, 0) * k
