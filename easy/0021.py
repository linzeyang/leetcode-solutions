"""21. Merge Two Sorted Lists"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val <= list2.val:
            new = ListNode(val=list1.val)
            list1 = list1.next
        else:
            new = ListNode(val=list2.val)
            list2 = list2.next

        head = new

        while list1 or list2:
            if not list1:
                new.next = ListNode(val=list2.val)
                list2 = list2.next
            elif not list2:
                new.next = ListNode(val=list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                new.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                new.next = ListNode(val=list2.val)
                list2 = list2.next

            new = new.next

        return head
