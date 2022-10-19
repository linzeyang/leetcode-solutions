"""2089. Find Target Indices After Sorting Array"""

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        out = []

        for idx, n in enumerate(sorted(nums)):
            if n == target:
                out.append(idx)
            elif out:
                break

        return out
