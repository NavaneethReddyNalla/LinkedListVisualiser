from tkinter import Frame

from logic.LinkedList import LinkedList
from logic.Node import Node
from .util import *
from ..components import *


class Visualiser(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.nodes = 0
        self.controller = controller
        self.draw_area = canvas(self)
        self.linked_list = LinkedList()

        self.create_widgets()
        self.styles()

    def create_widgets(self):
        self.configure_grid()

        self.draw_area.grid(row=0, column=0, rowspan=3, sticky="nsew")

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

        insert_pos = button(control_frame, "Insert at Position", command=None)
        insert_pos.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        delete_begin = button(control_frame, "Delete Begin", command=self.begin_delete)
        delete_begin.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        delete_end = button(control_frame, "Delete End", command=None)
        delete_end.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        delete_pos = button(control_frame, "Delete At Position", command=None)
        delete_pos.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

    def styles(self):
        self['background'] = "black"

    def configure_grid(self):
        for i in range(4):
            if i == 3:
                self.rowconfigure(i, weight=0)
            else:
                self.rowconfigure(i, weight=1)

        for i in range(1):
            self.columnconfigure(i, weight=1)

    def begin_insert(self):
        self.nodes += 1
        node = Node(self.nodes)

        draw_node(self.draw_area, node)

        if self.linked_list.head:
            shift_list(self.draw_area, self.linked_list.head)
        move_node_to(self.draw_area, node, 50, 150)

        self.linked_list.insert_begin(node)

    def end_insert(self):
        self.nodes += 1
        node = Node(self.nodes)

        draw_node(self.draw_area, node)

        move_node_to(self.draw_area, node, 50 + 100 * len(self.linked_list), 0)
        move_node_to(self.draw_area, node, 40 + 100 * len(self.linked_list), 150)

        self.linked_list.insert_end(node)

    def begin_delete(self):
        un_draw_node(self.draw_area, self.linked_list.head)
        shift_list(self.draw_area, self.linked_list.head.next, step=-1)

        self.linked_list.delete_begin()
