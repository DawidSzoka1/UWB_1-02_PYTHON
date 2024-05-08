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


def tabel_full(df, fields, object, bg_color, font_color, font, row_p, column_p, sticky_type="", x=0, y=0, start_row=0, end_row=0):
    for index, data_series in df.iterrows():
        for i, label in enumerate(fields):
            border = border_func(object, 1 + index, start_row+i, y=10, color=font_color,
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
