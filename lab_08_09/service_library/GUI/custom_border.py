import tkinter as tk


def border_func(on, row, col, y=0, x=0, color="", bg_color="", sticky_type=""):
    border = tk.Frame(on, highlightbackground=color,
                      highlightthickness=3, bd=0, bg=bg_color)
    border.grid(row=row, column=col, rowspan=1, padx=x, pady=y, sticky=sticky_type)
    return border
