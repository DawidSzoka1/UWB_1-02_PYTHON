import tkinter as tk
from custom_border import border_func


class Application(tk.Frame):
    def __init__(self, root):
        self.bg_color_1 = '#08172B'
        self.bg_color_2 = 'black'
        self.font_color_1 = '#CFCFA7'
        self.font_color_2 = 'white'
        self.font_style = "Georgia pro"

        super().__init__(root, bg=self.bg_color_1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=2)
        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_frame_list()
        self.create_frame_actions()

    def create_frame_list(self):
        self.frame_list = tk.Frame(
            self.main_frame,
            background=self.bg_color_1,
            width=1000,
            height=1000
        )
        self.frame_list.grid_columnconfigure(0, weight=1)
        self.frame_list.grid(row=0, column=0, sticky='nsew')
        self.frame_list.grid_propagate(False)
        self.label_frame_list()
        self.create_buttons_list()

    def label_frame_list(self):
        self.text_label = tk.Label(
            self.frame_list,
            bg="#08172B",
            text="LIBRARY",
            fg="#CFCFA7",
            font=("Georgia pro", 80)
        )
        self.text_label.grid(row=0, column=0, padx=(0, 250), pady=(50, 0), columnspan=4)

    def create_buttons_list(self):
        self.books_redirect = tk.Button(
            border_func(self.frame_list, 1, 2, (150, 10), (0, 250), self.font_color_1, self.bg_color_1),
            bg="#08172B", width=20,
            text="AVAILABLE BOOKS",
            fg=self.font_color_1,
            font=(self.font_style, 30, "bold")
        )
        self.books_redirect.grid(row=1, column=0)

        self.borrowed_books_redirect = tk.Button(
            border_func(self.frame_list, 2, 2, 10, (0, 250), self.font_color_1, self.bg_color_1),
            bg="#08172B",
            text="BORROWED BOOKS", fg=self.font_color_1,
            width=20,
            font=(self.font_style, 30, "bold")
        )
        self.borrowed_books_redirect.grid(row=2, column=0)

        self.customer_list_redirect = tk.Button(
            border_func(self.frame_list, 3, 2, (10, 150), (0, 250), self.font_color_1, self.bg_color_1),
            bg="#08172B", width=20,
            text="CUSTOMERS LIST",
            fg=self.font_color_1,
            font=(self.font_style, 30, "bold"),
        )
        self.customer_list_redirect.grid(row=3, column=0)

    def create_frame_actions(self):
        frame_actions = tk.Frame(
            self.main_frame,
            background=self.bg_color_2,
            width=500,
            height=self.main_frame.winfo_height())
        frame_actions.grid_columnconfigure(1, weight=1)
        frame_actions.grid(row=0, column=1, sticky='nsew')
        frame_actions.grid_propagate(False)


root = tk.Tk()
root.geometry('1500x1000')
app = Application(root)
root.mainloop()
