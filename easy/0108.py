"""
108. Convert Sorted Array to Binary Search Tree
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Very slow:
        # Runtime: 162 ms, faster than 7.97% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
        # Memory Usage: 15.7 MB, less than 31.52% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
        length = len(nums)
        if length == 1:
            return TreeNode(val=nums[0])

        if length == 2:
            return TreeNode(val=nums[1], left=TreeNode(val=nums[0]))

        mid_index = length // 2

        return TreeNode(
            val=nums[mid_index],
            left=self.sortedArrayToBST(nums=nums[:mid_index]),
            right=self.sortedArrayToBST(nums=nums[mid_index + 1 :]),
        )
