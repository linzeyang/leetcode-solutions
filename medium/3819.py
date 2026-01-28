"""3819. Rotate Non Negative Elements"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/rotate-non-negative-elements/
    Weekly Contest 486
    """

    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        non_neg_idxs: list[int] = []
        non_negs: list[int] = []

        for idx, num in enumerate(nums):
            if num >= 0:
                non_neg_idxs.append(idx)
                non_negs.append(num)

        if not non_negs:
            return nums

        k %= len(non_negs)

        for idx, num in zip(non_neg_idxs, non_negs[k:] + non_negs[:k], strict=True):
            nums[idx] = num

        return nums
