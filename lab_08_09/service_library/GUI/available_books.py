import tkinter as tk
from lab_08_09.service_library.GUI.custom_border import border_func
from lab_08_09.service_library.get_available_books import get_available_books


class AvailableBooks(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=1000
        )
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.frame.grid_propagate(False)
        self.label = tk.Label(
            self.frame,
            bg="#08172B",
            text="AVAILABLE BOOKS",
            fg="#CFCFA7",
            font=("Georgia pro", 70)

        )
        self.label.grid(row=0, column=1, sticky='nsew', pady=20, padx=(0, 200))
        self.back_to_home_page()
        self.tabel_label()

    def back_to_home_page(self):
        self.button_back = tk.Button(
            self.frame,
            bd=0,
            bg="#08172B", width=10,
            text="<",
            command=lambda: self.parent.show_frame(page=0),
            fg=self.parent.font_color_1,
            font=("Georgia pro", 30)
        )
        self.button_back.grid(row=0, column=0)

    def tabel_label(self):
        df = get_available_books()
        self.author_label = tk.Label(
            self.frame,
            text='AUTHOR',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2
        )
        self.author_label.grid(row=2, column=0, sticky='nsew')
        self.title_label = tk.Label(
            self.frame,
            text='TITLE',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2
        )
        self.title_label.grid(row=2, column=1, sticky='nsew')
        self.pages_label = tk.Label(
            self.frame,
            text='PAGES',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2
        )
        self.pages_label.grid(row=2, column=2, sticky='nsew')
