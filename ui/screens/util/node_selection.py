from tkinter import Canvas
from logic.LinkedList import LinkedList


class Selector:
    def __init__(self, canvas: Canvas, linked_list: LinkedList, deletion: bool = False):
        self.canvas = canvas
        self.linked_list = linked_list
        self.boxes = []
        self.deletion = deletion

        self.draw()

    def draw(self):
        curr = self.linked_list.head

        fill = "green" if not self.deletion else "red"

        while curr:
            coords = self.canvas.coords(curr.id)
            coords = (coords[0] - 5, coords[1] - 5, coords[2] + 5, coords[3] + 5)

            id = self.canvas.create_rectangle(*coords, outline="blue", activefill=fill, width=5)
            self.boxes.append(id)

            curr = curr.next
