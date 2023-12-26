from logic.LinkedList import LinkedList


class Selector:
    def __init__(self, screen, deletion: bool = False):
        self.screen = screen
        self.canvas = screen.draw_area
        self.linked_list = screen.linked_list
        self.deletion = deletion

        if self.linked_list.head:
            self.draw()
        else:
            self.screen.toggle_button_state()

    def draw(self):
        curr = self.linked_list.head

        fill = "green" if not self.deletion else "red"

        while curr:
            coords = self.canvas.coords(curr.id)
            coords = (coords[0] - 5, coords[1] - 5, coords[2] + 5, coords[3] + 5)

            curr.select_id = self.canvas.create_rectangle(*coords, outline="blue", activefill=fill, width=5)

            self.canvas.tag_bind(curr.select_id, "<Button>", self.handle_click)

            curr = curr.next

    def handle_click(self, event):
        curr = self.linked_list.head

        while curr:
            box_coords = self.canvas.coords(curr.id)

            if self.check_point(event.x, event.y, box_coords):
                self.delete_selections()
                self.screen.pos_insert(curr)
                break

            curr = curr.next

    def delete_selections(self):
        curr = self.linked_list.head

        while curr:
            self.canvas.delete(curr.select_id)
            curr.select_id = None
            curr = curr.next

    @staticmethod
    def check_point(x, y, box_coords):
        if box_coords[0] <= x <= box_coords[2] and box_coords[1] <= y <= box_coords[3]:
            return True

        return False
