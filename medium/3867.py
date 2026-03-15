"""3867. Sum of GCD of Formed Pairs"""

from math import gcd


class Solution:
    """
    https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
    Biweekly Contest 178
    """

    def gcdSum(self, nums: list[int]) -> int:
        current_max: int = 0
        prefix_gcd: list[int] = []

        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(gcd(num, current_max))

        prefix_gcd.sort()

        out: int = 0

        for idx in range(len(prefix_gcd) // 2):
            out += gcd(prefix_gcd[idx], prefix_gcd[-idx - 1])

        return out
