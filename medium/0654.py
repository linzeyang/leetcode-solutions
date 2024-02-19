"""654. Maximum Binary Tree"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self._build(nums=nums, start=0, end=len(nums) - 1)

    def _build(self, nums: list[int], start: int, end: int) -> TreeNode | None:
        if start > end:
            return None

        if start == end:
            return TreeNode(val=nums[start])

        val = nums[start]
        ind = start

        for idx in range(start + 1, end + 1):
            if nums[idx] > val:
                val = nums[idx]
                ind = idx

        return TreeNode(
            val=val,
            left=self._build(nums, start, ind - 1),
            right=self._build(nums, ind + 1, end),
        )
