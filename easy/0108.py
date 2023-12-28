"""108. Convert Sorted Array to Binary Search Tree"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._array_to_bst(nums, 0, len(nums) - 1)

    def _array_to_bst(
        self, nums: list[int], start: int, end: int
    ) -> Optional[TreeNode]:
        if start > end:
            return

        if start == end:
            return TreeNode(val=nums[start])

        idx = (start + end) // 2
        new_root = TreeNode(val=nums[idx])

        new_root.left = self._array_to_bst(nums, start, idx - 1)
        new_root.right = self._array_to_bst(nums, idx + 1, end)

        return new_root
