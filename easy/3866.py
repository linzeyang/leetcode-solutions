"""3866. First Unique Even Element"""

from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/first-unique-even-element/
    Biweekly Contest 178
    """

    def firstUniqueEven(self, nums: list[int]) -> int:
        counter: Counter[int] = Counter(num for num in nums if num & 1 == 0)

        for num, freq in counter.items():
            if freq == 1:
                return num

        return -1
