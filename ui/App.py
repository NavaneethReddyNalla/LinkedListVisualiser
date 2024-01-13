import tkinter as tk

from .components import *
from .screens import *


class App(tk.Tk):
    def __init__(self, title: str = "App", minsize: tuple = (500, 500)):
        super().__init__()
        self.title(title)
        self.minsize(*minsize)

        self.main_frame = frame(self)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.pack(fill='both', expand=True, side='top')

        self.frames = {}
        self.frame_keys = (MainMenu, Visualiser)

        self.create_frames()
        self.show_page(MainMenu)

    def create_frames(self):
        for one_frame in self.frame_keys:
            new_frame = one_frame(self.main_frame, self)
            self.frames[one_frame] = new_frame
            new_frame.grid(row=0, column=0, sticky="nsew")

    def destroy_frames(self):
        for f in self.frame_keys:
            self.frames[f].destroy()

    def show_page(self, page):
        if page == MainMenu:
            self.destroy_frames()
            self.create_frames()

        self.frames[page].tkraise()

    def run(self):
        self.mainloop()
