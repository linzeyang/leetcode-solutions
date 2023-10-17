"""707. Design Linked List"""

from typing import Optional


class Node:
    def __init__(self, val: int, next_node: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next_node


class MyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        node = self.head

        for _ in range(index):
            if not node.next:
                return -1

            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return

        node = self.head

        while node.next:
            node = node.next

        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        node = self.head

        for _ in range(index):
            if not node:
                return

            prev = node
            node = node.next

        prev.next = Node(val, node)

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        node = self.head

        for _ in range(index):
            if not node.next:
                return

            prev = node
            node = node.next

        prev.next = node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
