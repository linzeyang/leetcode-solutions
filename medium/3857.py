"""3857. Minimum Cost to Split into Ones"""


class Solution:
    """
    https://leetcode.com/problems/minimum-cost-to-split-into-ones/
    Weekly Contest 491
    """

    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2
