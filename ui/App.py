import tkinter as tk

from .components import *
from .screens import *


class App(tk.Tk):
    def __init__(self, title: str = "App", minsize: tuple = (500, 500)):
        super().__init__()
        self.title(title)
        self.minsize(*minsize)

        self.main_frame = frame(self)
        self.main_frame.pack(fill='both', expand=True, side='top')

        self.frames = {}
        self.frame_keys = (Visualiser, )

        for one_frame in self.frame_keys:
            new_frame = one_frame(self.main_frame, self)
            self.frames[one_frame] = new_frame
            new_frame.pack(fill="both", expand=True, side="top")

    def run(self):
        self.mainloop()
