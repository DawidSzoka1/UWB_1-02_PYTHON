import tkinter as tk
from GUI.books_page import Books
from GUI.home_page import MainPage
from GUI.all_customers import Customers
from GUI.add_book_page import AddBookPage
from GUI.add_user_page import AddUserPage
from GUI.borrow_book_page import BorrowBookPage
from GUI.return_book_page import ReturnBook


class Application(tk.Frame):
    def __init__(self, root):
        self.bg_color_1 = '#08172B'
        self.bg_color_2 = 'black'
        self.font_color_1 = '#CFCFA7'
        self.font_color_2 = 'white'
        self.font_style = "Georgia pro Regular"
        self.pages = [MainPage, Books, Books, Customers, AddBookPage, AddUserPage, BorrowBookPage, ReturnBook]

        super().__init__(root, bg=self.bg_color_1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.show_frame(0)

    def show_frame(self, page):
        frame = self.pages[page](self.main_frame)
        if page == 2:
            frame = self.pages[page](self.main_frame, True)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

