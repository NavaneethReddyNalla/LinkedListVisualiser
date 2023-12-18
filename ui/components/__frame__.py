from tkinter import Frame


def frame(parent) -> Frame:
    new_frame = Frame(parent)
    new_frame["background"] = "black"

    new_frame.grid_rowconfigure(0, weight=1)
    new_frame.grid_columnconfigure(0, weight=1)

    return new_frame
