"""
2. Add Two Numbers
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        adv = 0

        a = l1
        b = l2

        begin = ListNode(0)
        current = begin

        while a or b or adv:
            summ = (a.val if a else 0) + (b.val if b else 0) + adv
            adv = int(summ / 10)
            base = summ % 10
            new = ListNode(base)
            if begin == current:
                begin.next = new
            else:
                current.next = new

            current = new
            a = a.next if a else 0
            b = b.next if b else 0

        if adv:
            current.next = ListNode(adv)

        return begin.next
