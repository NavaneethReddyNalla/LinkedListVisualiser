from tkinter import Button


def button(parent, text="Button", command=None):
    new_button = Button(parent, text=text, command=command)

    return new_button
