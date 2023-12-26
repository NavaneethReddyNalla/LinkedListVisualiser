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

    def insert_pos(self, node: Node, pos_data=None):
        self.length += 1

        if self.head is None or pos_data is None:
            self.insert_begin(node)
        else:
            curr = self.head

            while curr.next and curr.data != pos_data:
                curr = curr.next

            node.next = curr
            node.prev = curr.prev
            curr.prev = node
            if node.prev:
                node.prev.next = node
            else:
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

            if self.head:
                self.head.prev = None

    def delete_end(self) -> None:
        if len(self) == 0:
            return None

        self.length -= 1

        curr = self.head
        while curr.next:
            curr = curr.next

        if curr.prev:
            curr.prev.next = None
            curr.prev = None
        else:
            self.head = None

    def __len__(self):
        return self.length

    def __str__(self):
        nodes = []

        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next

        return "->".join(nodes)
