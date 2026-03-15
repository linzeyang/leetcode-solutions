"""3868. Minimum Cost to Equalize Arrays Using Swaps"""

from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/
    Biweekly Contest 178
    """

    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counter1: Counter[int] = Counter()
        counter2: Counter[int] = Counter()
        counter_all: Counter[int] = Counter()

        for idx, num in enumerate(nums1):
            counter1[num] += 1
            counter2[nums2[idx]] += 1
            counter_all[num] += 1
            counter_all[nums2[idx]] += 1

        for freq in counter_all.values():
            if freq & 1:
                return -1

        out: int = 0

        for num, freq in counter1.items():
            if freq > counter2[num]:
                out += (freq - counter2[num]) // 2

        return out
