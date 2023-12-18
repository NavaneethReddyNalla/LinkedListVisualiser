import tkinter as tk


class App(tk.Tk):
    def __init__(self, title: str = "App", minsize: tuple = (500, 500)):
        super().__init__()
        self.title(title)
        self.minsize(*minsize)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both', expand=True, side='top')

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def run(self):
        self.mainloop()
