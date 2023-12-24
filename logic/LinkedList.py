from .Node import Node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.length: int = 0
    
    def insert_begin(self, node: Node) -> None:
        self.length += 1

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_end(self, node: Node) -> None:
        self.length += 1

        if self.head is None:
            self.head = node
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = node
            node.prev = curr

    def delete_begin(self) -> None:
        self.length -= 1
        self.head = self.head.next

    def __len__(self):
        return self.length
