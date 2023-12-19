from tkinter import Frame


class Visualiser(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller


