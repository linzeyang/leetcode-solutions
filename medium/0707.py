"""707. Design Linked List"""

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    nex = None


class MyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._length = 0

    def get(self, index: int) -> int:
        if index >= self._length:
            return -1

        if index == 0:
            return self._head.val

        if index == self._length - 1:
            return self._tail.val

        node = self._head

        for _ in range(index):
            node = node.nex

        return node.val

    def addAtHead(self, val: int) -> None:
        if self._head is None:
            self._head = self._tail = Node(val)
        else:
            node = Node(val)
            node.nex = self._head
            self._head = node
        self._length += 1

    def addAtTail(self, val: int) -> None:
        if self._tail is None:
            self._head = self._tail = Node(val)
        else:
            node = Node(val)
            self._tail.nex = node
            self._tail = node
        self._length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self._length:
            self.addAtTail(val)
            return

        prev = self._head

        for _ in range(index - 1):
            prev = prev.nex

        node = Node(val)
        node.nex = prev.nex
        prev.nex = node
        self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self._length:
            return

        if self._length == 1 and index == 0:
            self._head = self._tail = None
        elif index == 0:
            node = self._head
            self._head = node.nex
            node.nex = None
        else:
            prev = self._head

            for _ in range(index - 1):
                prev = prev.nex

            node = prev.nex
            prev.nex = node.nex
            node.nex = None

            if index == self._length - 1:
                self._tail = prev

        self._length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
