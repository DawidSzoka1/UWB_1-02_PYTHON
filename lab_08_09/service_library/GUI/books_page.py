import tkinter as tk
from lab_08_09.service_library.GUI.usefullfun import border_func
from lab_08_09.service_library.get_df_for_pages import get_books
from lab_08_09.service_library.GUI.usefullfun import back_to_home_page, label_tabel


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
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.tabel_label()
        self.tabel_info()
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.columnconfigure(0, weight=1)

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
