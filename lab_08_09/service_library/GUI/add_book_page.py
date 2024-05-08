import tkinter as tk
from lab_08_09.service_library.GUI.usefullfun import back_to_home_page
from lab_08_09.service_library.additionalfun import validate_int


class AddBookPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame_label = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1000,
            height=150
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

        self.label = tk.Label(
            self.frame_label,
            bg="#08172B",
            text="ADD BOOK",
            fg="#CFCFA7",
            font=("Georgia pro", 70)

        )
        self.label.grid(row=0, column=1, sticky='nsew', pady=20, padx=(0, 200))
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
        self.show_widgets()

    def show_widgets(self):
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.create_entry_fields()
        self.create_send_button()

    def create_entry_fields(self):
        fields = ['AUTHOR', 'TITLE', 'PAGES']
        self.author_entry = tk.Entry(self.entry_frame,
                                    bg=self.parent.bg_color_1,
                                    font=(self.parent.font_style, 50),
                                    insertbackground='white'
                                    )
        self.author_entry.grid(row=1, column=0, sticky='nsew')
        self.author_entry.config(fg=self.parent.font_color_1)
        self.author_label = tk.Label(
            self.entry_frame,
            text="AUTHOR",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.author_label.grid(row=0, column=0, sticky='nsew', padx=(0, 80))

        self.title_entry = tk.Entry(self.entry_frame,
                                    bg=self.parent.bg_color_1,
                                    font=(self.parent.font_style, 50),
                                    insertbackground='white'
                                    )
        self.title_entry.grid(row=3, column=0, sticky='nsew')
        self.title_entry.config(fg=self.parent.font_color_1)
        self.title_label = tk.Label(
            self.entry_frame,
            text="TITLE",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.title_label.grid(row=2, column=0, sticky='nsew', padx=(0, 80))

        validate_pages = self.register(validate_int)
        self.pages_entry = tk.Entry(self.entry_frame,
                                    bg=self.parent.bg_color_1,
                                    font=(self.parent.font_style, 50),
                                    insertbackground='white',
                                    validate='key',
                                    validatecommand=(validate_pages, '%P')
                                    )
        self.pages_entry.grid(row=5, column=0, sticky='nsew')
        self.pages_entry.config(fg=self.parent.font_color_1)
        self.pages_label = tk.Label(
            self.entry_frame,
            text="PAGES",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.pages_label.grid(row=4, column=0, sticky='nsew', padx=(0, 80))

    def create_send_button(self):
        pass
