"""1290. Convert Binary Number in a Linked List to Integer"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        out = 0
        node = head

        while node is not None:
            out = (out << 1) + node.val
            node = node.next

        return out
