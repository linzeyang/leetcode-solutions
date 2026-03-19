"""3870. Count Commas in Range"""


class Solution:
    """
    https://leetcode.com/problems/count-commas-in-range/
    Weekly Contest 493
    """

    def countCommas(self, n: int) -> int:
        return n - 999 if n >= 1_000 else 0
