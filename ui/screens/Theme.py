from tkinter import Frame

from ..styles import *


class Theme(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        pass
