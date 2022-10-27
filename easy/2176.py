"""2176. Count Equal and Divisible Pairs in an Array"""

from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dd = defaultdict(list)
        count = 0

        for idx, num in enumerate(nums):
            dd[num].append(idx)

        for lis in dd.values():
            if len(lis) < 2:
                continue

            for x, y in combinations(lis, 2):
                if (x * y) % k == 0:
                    count += 1

        return count
