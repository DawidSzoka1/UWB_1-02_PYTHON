import tkinter as tk


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