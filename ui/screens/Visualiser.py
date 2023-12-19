from tkinter import Frame

from ..components import *


class Visualiser(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        self.create_widgets()
        self.styles()

    def create_widgets(self):
        self.configure_grid()

        draw_area = canvas(self)
        # draw_area.pack(fill='both', expand=True, side="top")
        draw_area.grid(row=0, column=0, rowspan=3, sticky="nsew")

        control_frame = frame(self)
        # control_frame.pack(fill="both", expand=True, side="top")
        control_frame.grid(row=3, column=0, sticky="nsew")

        self.create_buttons(control_frame)

    def create_buttons(self, control_frame):
        pass

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
