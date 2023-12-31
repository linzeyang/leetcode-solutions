"""2196. Create Binary Tree From Descriptions"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = {}
        mapping_2 = {}

        for val, child_val, is_left in descriptions:
            if val not in mapping:
                node = TreeNode(val=val)
                mapping[val] = val
                mapping_2[val] = node
            else:
                node = mapping_2[val]

            if child_val not in mapping:
                child = TreeNode(val=child_val)
                mapping_2[child_val] = child
            else:
                child = mapping_2[child_val]

            mapping[child_val] = val

            if is_left:
                node.left = child
            else:
                node.right = child

        for k, v in mapping.items():
            if k == v:
                return mapping_2[k]
