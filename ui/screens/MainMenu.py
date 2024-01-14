from tkinter import Frame
from tkinter import messagebox

from ..components import *
from ..styles import *
from . import *


class MainMenu(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.buttons = set()

        self.configure_grid()
        self.create_widgets()
        self.style()

    def create_widgets(self):
        visualize = button(self, "Visualizer", command=lambda: self.controller.show_page(Visualizer))
        visualize.grid(row=0, column=1, sticky="sew", pady=10)
        self.buttons.add(visualize)

        about = button(self, "About", command=self.about_pop_up)
        about.grid(row=1, column=1, sticky="new", pady=10)
        self.buttons.add(about)

        close = button(self, "Quit", command=self.controller.close)
        close.grid(row=2, column=1, sticky="ew")
        self.buttons.add(close)

    @staticmethod
    def about_pop_up():
        message = "This app is created by the 2022-26 academic year students of VNR VJIET as their Python " \
            "Course Based Project. This project is primarily designed for helping new programmers learn " \
            "Linked list in a visual way for a better understanding. This project is intended to be very modular, " \
            "and can be easily expanded to visualize anything. This project also aims to show that vanilla python " \
            "can help build basically anything that you dream of if and you can just envision it.\n\n" \
            "Creators:\n" \
            "22071A6934 - Pabitha Kommineni\n" \
            "22071A6942 - Monitha Myneni\n" \
            "22071A6944 - Abhijeet Mukund NV\n" \
            "22071A6946 - Navaneeth Reddy Nalla\n\n" \
            "All belonging to CSE IoT 2022-26 batch"

        messagebox.showinfo(title="About", message=message)

    def style(self):
        self["background"] = PRIMARY_COLORS["frame"]

        for b in self.buttons:
            b["background"] = PRIMARY_COLORS["btn_primary"]
            b["height"] = 2

    def configure_grid(self):
        for i in range(3):
            self.rowconfigure(i, weight=1)

        for i in range(3):
            self.columnconfigure(i, weight=1)
