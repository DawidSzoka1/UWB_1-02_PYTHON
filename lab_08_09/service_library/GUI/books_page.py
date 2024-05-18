import tkinter as tk
from lab_08_09 import get_books
from lab_08_09 import back_to_home_page, label_tabel, tabel_full


class Books(tk.Frame):
    def __init__(self, parent, borrowed=False):
        super().__init__(parent)
        self.borrowed = borrowed
        self.parent = parent
        self.frame_label = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=100
        )
        self.frame_label.grid(row=0, column=0, sticky='nsew')
        self.frame_label.grid_propagate(False)
        label_text = "AVAILABLE BOOKS"
        if self.borrowed:
            label_text = "BORROWED BOOKS"

        self.label = tk.Label(
            self.frame_label,
            bg="#08172B",
            text=label_text,
            fg="#CFCFA7",
            font=(self.parent.font_style, 70)

        )
        self.label.grid(row=0, column=1, sticky='nsew', pady=20, padx=(0, 200))
        self.frame_tabel = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=900
        )
        self.frame_tabel.grid(row=1, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.columnconfigure(0, weight=1)
        self.show_widgets()

    def show_widgets(self):
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.tabel_label()
        self.tabel_info()

    def tabel_label(self):
        self.frame_tabel.columnconfigure(0, weight=1)
        self.frame_tabel.columnconfigure(1, weight=1)
        self.frame_tabel.columnconfigure(2, weight=1)
        label_text = ['AUTHOR', 'TITLE', 'PAGES']
        for i, label in enumerate(label_text):
            label_tabel(
                self.frame_tabel,
                label,
                self.parent.bg_color_2,
                self.parent.font_color_2,
                (self.parent.font_style, 20),
                0,
                i,
                'nsew'
            )

    def tabel_info(self):
        df = get_books(self.borrowed)
        label_text = ['AUTHOR', 'TITLE', 'PAGES']
        tabel_full(
            df,
            label_text,
            self.frame_tabel,
            self.parent.bg_color_1,
            self.parent.font_color_1,
            (self.parent.font_style, 20),
            0,
            0,
            'nsew',
            10,
            10,
        )
