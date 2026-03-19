"""3871. Count Commas in Range II"""


class Solution:
    """
    https://leetcode.com/problems/count-commas-in-range-ii/
    Weekly Contest 493
    """

    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0

        if n < 1_000_000:
            return n - 999

        if n < 1_000_000_000:
            return (n - 999_999) * 2 + self.countCommas(999_999)

        if n < 1_000_000_000_000:
            return (n - 999_999_999) * 3 + self.countCommas(999_999_999)

        if n < 1_000_000_000_000_000:
            return (n - 999_999_999_999) * 4 + self.countCommas(999_999_999_999)

        return (n - 999_999_999_999_999) * 5 + self.countCommas(999_999_999_999_999)
