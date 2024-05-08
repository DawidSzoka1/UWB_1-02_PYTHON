import tkinter as tk


def border_func(on, row, col, y=0, x=0, color="", bg_color="", sticky_type=""):
    border = tk.Frame(on, highlightbackground=color,
                      highlightthickness=3, bd=0, bg=bg_color)
    border.grid(row=row, column=col, rowspan=1, padx=x, pady=y, sticky=sticky_type)
    return border


def back_to_home_page(object, function, font_color, text="<"):
    button_back = tk.Button(
        object,
        bd=0,
        bg="#08172B", width=10,
        text=text,
        command=lambda: function(page=0),
        fg=font_color,
        font=("Georgia pro", 30)
    )
    button_back.grid(row=0, column=0)
    return button_back


def label_tabel(object, text, bg_color, font_color, font, row, column, sticky_type=""):
    author_label = tk.Label(
        object,
        text=text,
        bg=bg_color,
        fg=font_color,
        font=font
    )
    author_label.grid(row=row, column=column, sticky=sticky_type)
    return author_label
