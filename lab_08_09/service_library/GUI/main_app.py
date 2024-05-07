import tkinter as tk
from lab_08_09.service_library.GUI.available_books import AvailableBooks
from lab_08_09.service_library.GUI.home_page import MainPage


class Application(tk.Frame):
    def __init__(self, root):
        self.bg_color_1 = '#08172B'
        self.bg_color_2 = 'black'
        self.font_color_1 = '#CFCFA7'
        self.font_color_2 = 'white'
        self.font_style = "Georgia pro"
        self.pages = [MainPage, AvailableBooks]

        super().__init__(root, bg=self.bg_color_1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.show_frame(0)

    def show_frame(self, page):
        frame = self.pages[page](self.main_frame)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.columnconfigure(0, weight=1)
        frame.tkraise()

