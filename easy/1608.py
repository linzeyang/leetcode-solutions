"""1608. Special Array With X Elements Greater Than or Equal X"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ll = sorted(nums)

        if ll[0] >= len(ll):
            return len(ll)

        for idx, num in enumerate(ll):
            if num >= (x := len(ll) - idx):
                if x > ll[idx - 1]:
                    return x
                break

        return -1
