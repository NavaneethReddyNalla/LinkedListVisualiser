from .Node import Node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
    
    def insert_begin(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete_begin(self) -> None:
        self.head = self.head.next
