import tkinter as tk
from lab_08_09.service_library.GUI.usefullfun import back_to_home_page, border_func


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
        border = border_func(
            self.entry_frame,
            0,
            0,
            color=self.parent.bg_color_1,
            bg_color=self.parent.font_color_1,
            sticky_type='nsew'
        )
        self.title_entry = tk.Entry(border, bg=self.parent.bg_color_1, font=(self.parent.font_style, 20))
        self.title_entry.grid(row=0, column=0, sticky='nsew')
        self.title_entry.config(fg=self.parent.font_color_1)
        self.title_label = tk.Label(
            self.title_entry,
            text="TITLE",
            bg=self.parent.bg_color_1,
            font=(self.parent.font_style, 30)
        )

    def create_send_button(self):
        pass
