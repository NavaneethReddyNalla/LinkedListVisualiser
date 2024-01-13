from tkinter import Button

from ..styles import *


def button(parent, text="Button", command=None):
    new_button = Button(parent, text=text, command=command)
    new_button["foreground"] = PRIMARY_COLORS["btn_text"]

    return new_button
