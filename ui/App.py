import tkinter as tk


class App(tk.Tk):
    def __init__(self, title: str = "App", minsize: tuple = (500, 500)):
        super().__init__()
        self.title = title
        self.minsize = minsize

    def run(self):
        self.mainloop()
