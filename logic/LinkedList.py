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
        if len(self):
            self.length -= 1
            self.head = self.head.next

    def delete_end(self) -> None:
        if not len(self):
            return None

        self.length -= 1

        curr = self.head
        while curr.next:
            curr = curr.next

        if len(self) > 1:
            curr.prev.next = None
            curr.prev = None
        else:
            self.head = None

    def __len__(self):
        return self.length
