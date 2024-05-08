import tkinter as tk

from lab_08_09.service_library.GUI.usefullfun import back_to_home_page, border_func, use_backend_func
from lab_08_09.service_library.customerservice import add_customer


class AddUserPage(tk.Frame):
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
        self.create_send_button()
        self.create_entry()

    def create_entry(self):
        self.name_entry = tk.Entry(self.entry_frame,
                                   bg=self.parent.bg_color_1,
                                   font=(self.parent.font_style, 40),
                                   insertbackground='white'
                                   )
        self.name_entry.grid(row=1, column=0, sticky='nsew', padx=20, pady=5)
        self.name_entry.config(fg=self.parent.font_color_1)

        self.mail_entry = tk.Entry(self.entry_frame,
                                   bg=self.parent.bg_color_1,
                                   font=(self.parent.font_style, 40),
                                   insertbackground='white'
                                   )
        self.mail_entry.grid(row=3, column=0, sticky='nsew', padx=20, pady=5)
        self.mail_entry.config(fg=self.parent.font_color_1)

        self.phone_entry = tk.Entry(self.entry_frame,
                                    bg=self.parent.bg_color_1,
                                    font=(self.parent.font_style, 40),
                                    insertbackground='white',
                                    )

        self.phone_entry.grid(row=5, column=0, sticky='nsew', padx=20, pady=5)
        self.phone_entry.config(fg=self.parent.font_color_1)

        self.street_entry = tk.Entry(self.entry_frame,
                                     bg=self.parent.bg_color_1,
                                     font=(self.parent.font_style, 40),
                                     insertbackground='white',
                                     )

        self.street_entry.grid(row=7, column=0, sticky='nsew', padx=20, pady=5)
        self.street_entry.config(fg=self.parent.font_color_1)

        self.city_entry = tk.Entry(self.entry_frame,
                                   bg=self.parent.bg_color_1,
                                   font=(self.parent.font_style, 40),
                                   insertbackground='white',
                                   )

        self.city_entry.grid(row=9, column=0, sticky='nsew', padx=20, pady=5)
        self.city_entry.config(fg=self.parent.font_color_1)

        self.country_entry = tk.Entry(self.entry_frame,
                                      bg=self.parent.bg_color_1,
                                      font=(self.parent.font_style, 40),
                                      insertbackground='white',
                                      )

        self.country_entry.grid(row=11, column=0, sticky='nsew', padx=20, pady=5)
        self.country_entry.config(fg=self.parent.font_color_1)

    def create_label(self):
        self.main_label = tk.Label(
            self.frame_label,
            text='ADD USER',
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 80)
        )
        self.main_label.grid(row=0, column=1, sticky="nsew")
        self.name_label = tk.Label(
            self.entry_frame,
            text="NAME",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.name_label.grid(row=0, column=0, sticky='nsew', padx=(0, 80))

        self.mail_label = tk.Label(
            self.entry_frame,
            text="E-MAIL",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.mail_label.grid(row=2, column=0, sticky='nsew', padx=(0, 80))

        self.phone_label = tk.Label(
            self.entry_frame,
            text="PHONE",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.phone_label.grid(row=4, column=0, sticky='nsew', padx=(0, 80))

        self.street_label = tk.Label(
            self.entry_frame,
            text="STREET",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.street_label.grid(row=6, column=0, sticky='nsew', padx=(0, 80))

        self.city_label = tk.Label(
            self.entry_frame,
            text="CITY",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.city_label.grid(row=8, column=0, sticky='nsew', padx=(0, 80))

        self.country_label = tk.Label(
            self.entry_frame,
            text="COUNTRY",
            bg=self.parent.bg_color_1,
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30)
        )
        self.country_label.grid(row=10, column=0, sticky='nsew', padx=(0, 80))

    def create_send_button(self):
        self.send_frame.rowconfigure(0, weight=1)
        self.send_backend = tk.Button(
            border_func(self.send_frame, 0, 2, (10, 150), (40, 0), self.parent.font_color_2, self.parent.bg_color_2),
            bg=self.parent.bg_color_2,
            width=15,
            height=4,
            text="ADD",
            command=lambda: use_backend_func(add_customer,
                                             self.name_entry.get(),
                                             self.mail_entry.get(),
                                             self.phone_entry.get(),
                                             self.street_entry.get(),
                                             self.city_entry.get(),
                                             self.country_entry.get()
                                             ),
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold")
        )
        self.send_backend.grid(row=0, column=0)
