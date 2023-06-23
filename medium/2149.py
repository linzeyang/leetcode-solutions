"""2149. Rearrange Array Elements by Sign"""

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        out = []

        for idx in range(len(pos)):
            out.append(pos[idx])
            out.append(neg[idx])

        return out
