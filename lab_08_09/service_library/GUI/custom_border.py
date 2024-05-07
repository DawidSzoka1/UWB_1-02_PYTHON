import tkinter as tk


def border_func(on, row, col, y, x=None, color="", bg_color=""):
    border = tk.Frame(on, highlightbackground=color,
                      highlightthickness=3, bd=0, bg=bg_color)
    border.grid(row=row, column=col, rowspan=1, padx=x, pady=y)
    return border
