import tkinter as tk
from lab_08_09.service_library.GUI.usefullfun import back_to_home_page, label_tabel, tabel_full, border_func
from lab_08_09.service_library.get_df_for_pages import get_customers


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
        self.rowconfigure(1, weight=8)
        self.columnconfigure(0, weight=1)
        self.create_tabel_label()
        self.create_rows_tabel()

    def create_tabel_label(self):
        self.frame_tabel.columnconfigure(0, weight=1)
        self.frame_tabel.columnconfigure(1, weight=1)
        self.frame_tabel.columnconfigure(2, weight=1)
        self.frame_tabel.columnconfigure(3, weight=1)
        self.frame_tabel.columnconfigure(4, weight=1)
        self.frame_tabel.columnconfigure(5, weight=1)
        label_text = ['NAME', 'E-MAIL', 'PHONE', 'STREET', 'CITY', 'COUNTRY']
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

    def create_rows_tabel(self):
        text = [['NAME', 'E-MAIL', 'PHONE'], ['STREET', 'CITY', 'COUNTRY']]
        for index, df in enumerate(get_customers()):
            tabel_full(
                df,
                text[index],
                self.frame_tabel,
                self.parent.bg_color_1,
                self.parent.font_color_1,
                (self.parent.font_style, 20),
                0,
                0,
                'nsew',
                10,
                10,
                start_row=index*3
            )
