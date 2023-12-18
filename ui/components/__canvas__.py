from tkinter import Canvas
from tkinter import SUNKEN


def canvas(parent, dim: tuple = (500, 300), bg_color="white"):
    new_canvas = Canvas(parent, width=dim[0], height=dim[1], background=bg_color, relief=SUNKEN)
    return new_canvas
