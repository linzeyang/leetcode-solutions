"""2640. Find the Score of All Prefixes of an Array"""

from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        out: list[int] = []

        prev = convs = 0

        for num in nums:
            prev = max(num, prev)
            convs += num + prev
            out.append(convs)

        return out
