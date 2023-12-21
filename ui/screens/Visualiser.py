from tkinter import Frame

from logic.LinkedList import LinkedList
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

        control_frame = frame(self)
        control_frame.grid(row=3, column=0, sticky="nsew", padx=10)
        # control_frame.pack_propagate(False)

        self.create_buttons(control_frame)

    def create_buttons(self, control_frame):
        insert_beg = button(control_frame, "Insert Begin", command=self.begin_insert)
        insert_beg.pack(side="left", expand=True, fill="both", padx=5, pady=5)

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
        self.linked_list.insert_begin(self.nodes)

        draw_linked_list(self.draw_area, self.linked_list)
