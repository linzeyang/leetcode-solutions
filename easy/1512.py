"""1512. Number of Good Pairs"""

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        out = 0
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                out += dic[num]
                dic[num] += 1

        return out
