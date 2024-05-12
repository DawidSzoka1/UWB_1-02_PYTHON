import tkinter as tk
from lab_08_09.service_library.GUI.usefullfun import border_func


class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.load_main_widgets()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def load_main_widgets(self):
        self.create_frame_list()
        self.create_frame_actions()

    def create_frame_list(self):
        self.frame_list = tk.Frame(
            self,
            background=self.parent.bg_color_1,
            width=1000,
            height=1000
        )
        self.frame_list.grid_columnconfigure(0, weight=1)
        self.frame_list.grid(row=0, column=0, sticky='nsew')
        self.frame_list.grid_propagate(False)
        self.label_frame_list()
        self.list_redirect()

    def label_frame_list(self):
        self.text_label = tk.Label(
            self.frame_list,
            bg="#08172B",
            text="LIBRARY",
            fg="#CFCFA7",
            font=("Georgia pro", 80)
        )
        self.text_label.grid(row=0, column=0, padx=(0, 250), pady=(50, 0), columnspan=4)

    def list_redirect(self):
        self.books_redirect = tk.Button(
            border_func(self.frame_list, 1, 2, (150, 10), (0, 300), self.parent.font_color_1, self.parent.bg_color_1),
            bg="#08172B", width=20,
            text="AVAILABLE BOOKS",
            command=lambda: self.parent.show_frame(page=1),
            fg=self.parent.font_color_1,
            font=(self.parent.font_style, 30, "bold")
        )
        self.books_redirect.grid(row=1, column=0)

        self.borrowed_books_redirect = tk.Button(
            border_func(self.frame_list, 2, 2, 10, (0, 300), self.parent.font_color_1, self.parent.bg_color_1),
            bg="#08172B",
            text="BORROWED BOOKS",
            fg=self.parent.font_color_1,
            command=lambda: self.parent.show_frame(page=2),
            width=20,
            font=(self.parent.font_style, 30, "bold")
        )
        self.borrowed_books_redirect.grid(row=2, column=0)

        self.customer_list_redirect = tk.Button(
            border_func(self.frame_list, 3, 2, (10, 150), (0, 300), self.parent.font_color_1, self.parent.bg_color_1),
            bg="#08172B",
            width=20,
            text="CUSTOMERS LIST",
            fg=self.parent.font_color_1,
            command=lambda: self.parent.show_frame(page=3),
            font=(self.parent.font_style, 30, "bold"),
        )
        self.customer_list_redirect.grid(row=3, column=0)

    def create_frame_actions(self):
        self.frame_actions = tk.Frame(
            self,
            background=self.parent.bg_color_2,
            width=500,
            height=1000)
        self.frame_actions.grid_columnconfigure(1, weight=1)
        self.frame_actions.grid(row=0, column=1, sticky='nsew')
        self.frame_actions.grid_propagate(False)
        self.redirect_actions()

    def redirect_actions(self):
        self.add_book_redirect = tk.Button(
            border_func(self.frame_actions, 0, 0, (100, 10), (80, 0), color=self.parent.font_color_2,
                        bg_color=self.parent.bg_color_2),
            text="ADD \nBOOK",
            width=20,
            height=5,
            background=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold"),
            command=lambda: self.parent.show_frame(4)
        )
        self.add_book_redirect.grid(row=0, column=0)

        self.add_user_redirect = tk.Button(
            border_func(self.frame_actions, 1, 0, 5, (80, 0), color=self.parent.font_color_2,
                        bg_color=self.parent.bg_color_2),
            text="ADD \nUSER",
            width=20,
            height=5,
            background=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold"),
            command=lambda: self.parent.show_frame(5)
        )
        self.add_user_redirect.grid(row=0, column=0)
        self.borrow_book_redirect = tk.Button(
            border_func(self.frame_actions, 2, 0, 5, (80, 0), color=self.parent.font_color_2,
                        bg_color=self.parent.bg_color_2),
            text="BORROW \nBOOK",
            width=20,
            height=5,
            background=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold"),
            command=lambda: self.parent.show_frame(page=6)
        )
        self.borrow_book_redirect.grid(row=0, column=0)

        self.return_book_redirect = tk.Button(
            border_func(self.frame_actions, 3, 0, 5, (80, 0), color=self.parent.font_color_2,
                        bg_color=self.parent.bg_color_2),
            text="RETURN \nBOOK",
            width=20,
            height=5,
            background=self.parent.bg_color_2,
            fg=self.parent.font_color_2,
            font=(self.parent.font_style, 20, "bold"),
            command=lambda: self.parent.show_frame(page=7)
        )
        self.return_book_redirect.grid(row=0, column=0)
