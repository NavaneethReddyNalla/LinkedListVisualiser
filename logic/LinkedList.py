from .Node import Node


class LinkedList:
    def __init__(self):
        self.head: Node = None
    
    def insert_begin(self, data: int) -> None:
        if self.head is None:
            self.head = Node(data)
        else:
            new_node: Node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_begin(self) -> None:
        self.head = self.head.next
