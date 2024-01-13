from tkinter import Frame

from ..components import *
from ..styles import *


class MainMenu(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.buttons = set()

        self.configure_grid()
        self.create_widgets()
        self.style()

    def create_widgets(self):
        visualize = button(self, "Visualizer")
        visualize.grid(row=0, column=1, sticky="sew", pady=10)
        self.buttons.add(visualize)

        about = button(self, "About")
        about.grid(row=1, column=1, sticky="new", pady=10)
        self.buttons.add(about)

        close = button(self, "Quit")
        close.grid(row=2, column=1, sticky="ew")
        self.buttons.add(close)

    def style(self):
        self["background"] = PRIMARY_COLORS["frame"]

        for b in self.buttons:
            b["background"] = PRIMARY_COLORS["btn_primary"]

    def configure_grid(self):
        for i in range(3):
            self.rowconfigure(i, weight=1)

        for i in range(3):
            self.columnconfigure(i, weight=1)
