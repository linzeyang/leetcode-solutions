"""
234. Palindrome Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Very slow:
        # Runtime: 2400 ms, faster than 5.01% of Python3 online submissions for Palindrome Linked List.
        # Memory Usage: 46.8 MB, less than 37.45% of Python3 online submissions for Palindrome Linked List.
        lis = []
        node = head

        while node is not None:
            lis.append(node.val)
            node = node.next

        for i in range(len(lis) // 2):
            if lis[i] != lis[-i - 1]:
                return False

        return True
