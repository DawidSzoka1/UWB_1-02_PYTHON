import tkinter as tk
from lab_08_09.service_library.GUI.custom_border import border_func
from lab_08_09.service_library.get_books import get_books


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
            font=("Georgia pro", 70)

        )
        self.label.grid(row=0, column=1, sticky='nsew', pady=20, padx=(0, 200))
        self.frame_tabel = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=900
        )
        self.frame_tabel.grid(row=1, column=0, sticky='nsew')
        self.back_to_home_page()
        self.tabel_label()
        self.tabel_info()
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def back_to_home_page(self):
        self.button_back = tk.Button(
            self.frame_label,
            bd=0,
            bg="#08172B", width=10,
            text="<",
            command=lambda: self.parent.show_frame(page=0),
            fg=self.parent.font_color_1,
            font=("Georgia pro", 30)
        )
        self.button_back.grid(row=0, column=0)

    def tabel_label(self):
        df = get_books(self.borrowed)
        self.frame_label.columnconfigure(0, weight=1)
        self.frame_label.columnconfigure(1, weight=1)
        self.frame_label.columnconfigure(2, weight=1)
        self.author_label = tk.Label(
            self.frame_tabel,
            text='AUTHOR',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20)
        )
        self.author_label.grid(row=0, column=0, sticky='nsew')
        self.title_label = tk.Label(
            self.frame_tabel,
            text='TITLE',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20)

        )
        self.title_label.grid(row=0, column=1, sticky='nsew')
        self.pages_label = tk.Label(
            self.frame_tabel,
            text='PAGES',
            bg=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20)
        )
        self.pages_label.grid(row=0, column=2, sticky='nsew')

    def tabel_info(self):
        df = get_books(self.borrowed)
        for index, book in df.iterrows():
            author_border = border_func(self.frame_tabel, 1 + index, 0, y=10, color=self.parent.font_color_1,
                                        bg_color=self.parent.bg_color_1, sticky_type='nsew')
            author_border.grid_rowconfigure(0, weight=1)
            author_border.grid_columnconfigure(0, weight=1)
            author = tk.Label(
                author_border,
                text=f'{book["AUTHOR"]}',
                bg=self.parent.bg_color_1,
                fg=self.parent.font_color_1,
            )
            author.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            title_border = border_func(self.frame_tabel, 1+index, 1, y=10, color=self.parent.font_color_1,
                                       bg_color=self.parent.bg_color_1, sticky_type='nsew')
            title_border.grid_rowconfigure(0, weight=1)
            title_border.grid_columnconfigure(0, weight=1)
            title = tk.Label(
                title_border,
                text=f'{book["TITLE"]}',
                pady=50,
                bg=self.parent.bg_color_1,
                fg=self.parent.font_color_1
            )
            title.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            pages_border = border_func(self.frame_tabel, 1 + index, 2, y=10, color=self.parent.font_color_1,
                                       bg_color=self.parent.bg_color_1, sticky_type='nsew')
            pages_border.grid_rowconfigure(0, weight=1)
            pages_border.grid_columnconfigure(0, weight=1)
            pages = tk.Label(
                pages_border,
                text=f'{book["PAGES"]}',
                pady=50,
                bg=self.parent.bg_color_1,
                fg=self.parent.font_color_1
            )
            pages.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
