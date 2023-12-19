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

    def run(self):
        self.mainloop()
