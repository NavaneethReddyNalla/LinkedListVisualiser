class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node | None = None
        self.prev: Node | None = None
        self.id: int | None = None
        self.data_id: int | None = None
        self.arrow_id: int | None = None
