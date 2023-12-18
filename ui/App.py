import tkinter as tk

from .components import *


class App(tk.Tk):
    def __init__(self, title: str = "App", minsize: tuple = (500, 500)):
        super().__init__()
        self.title(title)
        self.minsize(*minsize)

        self.main_frame = frame(self)
        self.main_frame.pack(fill='both', expand=True, side='top')

        self.canvas = canvas(self.main_frame)
        self.canvas.pack(fill="both", expand=True, side="top")

    def run(self):
        self.mainloop()
