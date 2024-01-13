from tkinter import Canvas
from tkinter import SUNKEN

from ..styles import *


def canvas(parent, dim: tuple = (500, 500)):
    new_canvas = Canvas(parent, width=dim[0], height=dim[1], background=PRIMARY_COLORS["canvas"], relief=SUNKEN)
    return new_canvas
