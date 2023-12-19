from tkinter import Frame


def frame(parent, dim: tuple = (500, 200)) -> Frame:
    new_frame = Frame(parent, width=dim[0], height=dim[1])
    new_frame["background"] = "black"

    new_frame.grid_rowconfigure(0, weight=1)
    new_frame.grid_columnconfigure(0, weight=1)

    return new_frame
