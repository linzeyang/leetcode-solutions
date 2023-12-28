"""235. Lowest Common Ancestor of a Binary Search Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root.val in {p.val, q.val}:
            return root

        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)
