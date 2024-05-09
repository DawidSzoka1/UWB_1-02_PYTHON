import tkinter as tk
from tkinter import messagebox


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


def tabel_rows(object, text, bg_color, font_color, font, row_p, column_p, sticky_type="", x=0, y=0):
    row = tk.Label(
        object,
        text=text,
        bg=bg_color,
        fg=font_color,
        font=font
    )
    row.grid(row=row_p, column=column_p, sticky=sticky_type, padx=x, pady=y)
    return row


def tabel_full(df, fields, object, bg_color, font_color, font, row_p, column_p, sticky_type="", x=0, y=0, start_row=0,
               end_row=0):
    for index, data_series in df.iterrows():
        for i, label in enumerate(fields):
            border = border_func(object, 1 + index, start_row + i, y=10, color=font_color,
                                 bg_color=bg_color, sticky_type='nsew')
            border.grid_rowconfigure(0, weight=1)
            border.grid_columnconfigure(0, weight=1)
            tabel_rows(
                border,
                f'{data_series[label]}',
                bg_color,
                font_color,
                font,
                row_p,
                column_p,
                sticky_type,
                x,
                y
            )


def show_message(type, title, message):
    if type == 'info':
        tk.messagebox.showinfo(title, message)
    else:
        tk.messagebox.showwarning(title, message)


def use_backend_func(func, *args):
    check = func(*args)
    if check['type'] == 'success':
        messagebox.showinfo('Success', f'{check["message"]}')
    else:
        messagebox.showerror('ERROR', f'{check["message"]}')


def check_user_to_id_and_backend(name, df, func, *args):
    if name == '' or len(args) == 0:
        messagebox.showinfo('info', 'All fields are required.')
    else:
        try:
            get_id = df[df["NAME"] == name.title()].index.values[0]
        except IndexError:
            messagebox.showerror('ERROR', f'{name.title()} we dont have that user')
        else:
            use_backend_func(func, get_id, *args)
