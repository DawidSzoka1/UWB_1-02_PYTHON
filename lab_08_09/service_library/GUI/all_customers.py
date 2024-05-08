import tkinter as tk
from lab_08_09.service_library.GUI.back_to_main_page_button import back_to_home_page


class Customers(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame_label = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=150
        )
        self.frame_label.grid(row=0, column=0, sticky='nsew')
        self.frame_label.grid_propagate(False)
        self.label = tk.Label(
            self.frame_label,
            bg="#08172B",
            text="LIST OF CUSTOMERS",
            fg="#CFCFA7",
            font=("Georgia pro", 70)

        )
        self.label.grid(row=0, column=1, sticky='nsew', pady=20, padx=(0, 200))
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.frame_tabel = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1500,
            height=900
        )
        self.frame_tabel.grid(row=1, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)


