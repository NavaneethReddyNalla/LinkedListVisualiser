from tkinter import Frame

from ..styles import *


def frame(parent, dim: tuple = (500, 200), grid: tuple = None) -> Frame:
    new_frame = Frame(parent, width=dim[0], height=dim[1])
    new_frame["background"] = PRIMARY_COLORS["frame"]

    if not grid:
        new_frame.grid_rowconfigure(0, weight=1)
        new_frame.grid_columnconfigure(0, weight=1)
    else:
        for i in range(grid[0]):
            new_frame.grid_rowconfigure(i, weight=1)
        for i in range(grid[1]):
            new_frame.grid_columnconfigure(i, weight=1)

    return new_frame
