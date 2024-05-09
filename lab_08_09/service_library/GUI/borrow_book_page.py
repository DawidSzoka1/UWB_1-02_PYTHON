import tkinter as tk
from tkinter import messagebox

from lab_08_09.service_library.GUI.usefullfun import back_to_home_page, border_func, use_backend_func
from lab_08_09.service_library.customerservice import borrow_book
from lab_08_09.service_library.get_df_for_pages import get_customers


class BorrowBookPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame_label = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1000,
            height=200
        )
        self.frame_label.grid(row=0, column=0, sticky='nsew')
        self.frame_label.grid_propagate(False)

        self.send_frame = tk.Frame(
            self,
            bg=self.parent.bg_color_2,
            width=500,
            height=1000
        )
        self.send_frame.grid(row=0, column=1, sticky='nsew', rowspan=2)

        self.entry_frame = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1000,
            height=900
        )
        self.entry_frame.grid(row=1, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.load_widgets()

    def load_widgets(self):
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.create_label()
        self.create_entry()
        self.create_send_button()

    def create_label(self):
        self.main_label = tk.Label(
            self.frame_label,
            text="BORROW BOOKS",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 65)
        )
        self.main_label.grid(row=0, column=1, sticky='nsew')

        self.user_label = tk.Label(
            self.entry_frame,
            text="USER NAME",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.user_label.grid(row=0, column=0, sticky='nsew')

        self.books_label = tk.Label(
            self.entry_frame,
            text="BOOKS TITLES np:('title1','title2')",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30),
        )
        self.books_label.grid(row=2, column=0, sticky='nsew', pady=(20, 0))

    def create_entry(self):
        self.user_entry = tk.Entry(
            self.entry_frame,
            bg=self.parent.bg_color_1,
            font=(self.parent.font_style, 40),
            insertbackground='white'
        )
        self.user_entry.grid(row=1, column=0, sticky='nsew')

        self.books_entry = tk.Entry(
            self.entry_frame,
            bg=self.parent.bg_color_1,
            font=(self.parent.font_style, 40),
            insertbackground='white'
        )
        self.books_entry.grid(row=3, column=0, sticky='nsew')

    def create_send_button(self):

        df, _ = get_customers()

        self.send_frame.rowconfigure(0, weight=1)
        self.send_backend = tk.Button(
            border_func(self.send_frame, 0, 2, (10, 150), (40, 0), self.parent.font_color_2, self.parent.bg_color_2),
            bg=self.parent.bg_color_2,
            width=15,
            height=4,
            text="ADD",
            command=lambda: use_backend_func(
                borrow_book,
                df[df['NAME'] == self.user_entry.get()].index.values[0],
                *self.books_entry.get().split(',')
            ),
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold")
        )
        self.send_backend.grid(row=0, column=0)
