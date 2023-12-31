"""109. Convert Sorted List to Binary Search Tree"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        prev = None
        original_head = slow = head
        fast = head.next

        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next

            prev = slow
            slow = slow.next

        root = TreeNode(val=slow.val)
        root.right = self.sortedListToBST(slow.next)

        if prev:
            prev.next = None

        if original_head is not slow:
            root.left = self.sortedListToBST(original_head)

        return root
