"""234. Palindrome Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        vals = []
        node = head

        while node:
            vals.append(node.val)
            node = node.next

        for idx in range(len(vals) // 2):
            if vals[idx] != vals[-idx - 1]:
                return False

        return True
