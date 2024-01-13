from tkinter import Frame
from tkinter import Scrollbar

from tkinter import Label

from tkinter import HORIZONTAL

from logic.LinkedList import LinkedList
from logic.Node import Node
from .util import *
from ..components import *
from ..styles import *


class Visualiser(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.nodes = 0
        self.controller = controller
        self.draw_frame = frame(self)
        self.draw_area = canvas(self.draw_frame)
        self.linked_list = LinkedList()
        self.buttons = {}

        self.create_widgets()
        self.styles()

    def create_widgets(self):
        self.configure_grid()

        heading = Label(self, text="Linked List Visualizer", font=("Helvetica", 16, "bold"), background="black",
                        fg="white")
        heading.grid(row=0, column=0, sticky="new")

        self.draw_area.create_text(75, 220, font=("Helvetica", 14, "bold"), text="Start", fill="black")

        self.draw_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.draw_area.pack(expand=True, fill="both", side="top")

        scrollbar = Scrollbar(self.draw_frame, orient=HORIZONTAL, command=self.draw_area.xview)
        scrollbar.pack(fill="x", side="top")

        self.draw_area.config(xscrollcommand=scrollbar.set)

        control_frame = frame(self, grid=(3, 3))
        control_frame.grid(row=3, column=0, sticky="nsew", padx=10)
        # control_frame.pack_propagate(False)

        self.create_buttons(control_frame)

    def create_buttons(self, control_frame):
        insert_beg = button(control_frame, "Insert Begin", command=self.begin_insert)
        # insert_beg.pack(side="left", expand=True, fill="both", padx=5, pady=5) # not using pack for more control
        insert_beg.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        insert_end = button(control_frame, "Insert End", command=self.end_insert)
        insert_end.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        insert_pos = button(control_frame, "Insert at Position", command=self.select_node)
        insert_pos.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        delete_beg = button(control_frame, "Delete Begin", command=self.begin_delete)
        delete_beg.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        delete_end = button(control_frame, "Delete End", command=self.end_delete)
        delete_end.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        delete_pos = button(control_frame, "Delete At Position", command=lambda: self.select_node(deletion=True))
        delete_pos.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.buttons['insert_beg'] = insert_beg
        self.buttons['insert_end'] = insert_end
        self.buttons['insert_pos'] = insert_pos
        self.buttons['delete_beg'] = delete_beg
        self.buttons['delete_end'] = delete_end
        self.buttons['delete_pos'] = delete_pos

    def styles(self):
        self['background'] = PRIMARY_COLORS["frame"]

    def configure_grid(self):
        for i in range(4):
            if i == 3:
                self.rowconfigure(i, weight=0)
            else:
                self.rowconfigure(i, weight=1)

        for i in range(1):
            self.columnconfigure(i, weight=1)

    def begin_insert(self):
        self.toggle_button_state()
        self.nodes += 1
        node = Node(self.nodes)

        draw_node(self.draw_area, node)

        if self.linked_list.head:
            shift_list(self.draw_area, self.linked_list.head)
        move_node_to(self.draw_area, node, 50, 150)

        self.linked_list.insert_begin(node)
        self.toggle_button_state()
        self.adjust_scroll_region()

    def end_insert(self):
        self.toggle_button_state()
        self.nodes += 1
        node = Node(self.nodes)

        draw_node(self.draw_area, node)

        move_node_to(self.draw_area, node, 50 + 100 * len(self.linked_list), 10)
        move_node_to(self.draw_area, node, 50 + 100 * len(self.linked_list), 150)

        self.linked_list.insert_end(node)
        self.toggle_button_state()
        self.adjust_scroll_region()

    def select_node(self, deletion=False):
        self.toggle_button_state()
        Selector(self, deletion=deletion)

    def pos_insert(self, node: Node):
        self.nodes += 1
        new_node = Node(self.nodes)

        draw_node(self.draw_area, new_node)

        x_node = self.draw_area.coords(node.id)[0]
        y_node = self.draw_area.coords(node.id)[1]

        move_node_to(self.draw_area, new_node, x_node, 10)
        shift_list(self.draw_area, node)
        move_node_to(self.draw_area, new_node, x_node, y_node)

        self.linked_list.insert_pos(new_node, node.data)
        self.toggle_button_state()
        self.adjust_scroll_region()

    def begin_delete(self):
        self.toggle_button_state()

        if len(self.linked_list):
            move_node_to(self.draw_area, self.linked_list.head, 50, 10)
            shift_list(self.draw_area, self.linked_list.head.next, step=-1)
            un_draw_node(self.draw_area, self.linked_list.head)

        self.linked_list.delete_begin()
        self.toggle_button_state()
        self.adjust_scroll_region()

    def end_delete(self):
        self.toggle_button_state()

        if len(self.linked_list):
            delete_node = self.linked_list.head

            while delete_node.next:
                delete_node = delete_node.next

            curr_x = self.draw_area.coords(delete_node.id)[0]

            move_node_to(self.draw_area, delete_node, curr_x, 10)
            un_draw_node(self.draw_area, delete_node)

            self.linked_list.delete_end()

        self.toggle_button_state()
        self.adjust_scroll_region()

    def pos_delete(self, node: Node):
        current_x = self.draw_area.coords(node.id)[0]

        move_node_to(self.draw_area, node, current_x, 10)
        shift_list(self.draw_area, node.next, step=-1)
        un_draw_node(self.draw_area, node)

        self.linked_list.delete_pos(node.data)
        self.toggle_button_state()
        self.adjust_scroll_region()

    def toggle_button_state(self):
        if self.buttons['insert_beg']['state'] == "normal":
            for _button in self.buttons:
                self.buttons[_button]["state"] = "disabled"
        else:
            for _button in self.buttons:
                self.buttons[_button]["state"] = "normal"

    def adjust_scroll_region(self):
        # self.draw_area.config(scrollregion=self.draw_area.bbox("all"))
        self.draw_area.config(scrollregion=(0, 0, (len(self.linked_list) + 1) * 100, 500))
