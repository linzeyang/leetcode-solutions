"""328. Odd Even Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        odd = head
        even_head = even = head.next

        if not even_head:
            return head

        current = even_head.next

        is_odd = False

        while current:
            is_odd = not is_odd

            if is_odd:
                odd.next = current
                odd = current
            else:
                even.next = current
                even = current

            current = current.next

        odd.next = even_head

        if even.next:
            even.next = None

        return head
