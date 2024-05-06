import customerservice
import rejestbook
import tkinter as tk
from tkinter import messagebox
from additionalfun import read_csv
import pandas as pd


def custom_border(on, row, col, y, x=None, color="", bg_color=""):
    border = tk.Frame(on, highlightbackground=color,
                      highlightthickness=3, bd=0, bg=bg_color)
    border.grid(row=row, column=col, rowspan=1, padx=x, pady=y)
    return border


def change_height_width(object, width, height):
    pass


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System")
        self.geometry("1500x1000")
        self.books = []
        self.customer_frame = 0
        self.frame1 = tk.Frame(self, bg="#08172B", height=self.winfo_height(), width=990)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame1.grid_propagate(False)
        self.white_bar = tk.Frame(self.frame1, bg="white", width=5, height=self.winfo_height())
        self.white_bar.pack(fill="y", side="left", padx=30)

        self.text_label = tk.Label(self.frame1, bg="#08172B", text="LIBRARY", fg="#CFCFA7", font=("Georgia pro", 80))
        self.text_label.grid(row=0, column=2, padx=80, pady=(50, 0))

        self.books_redirect = tk.Button(
            custom_border(self.frame1, 1, 2, (150, 10), 80, "#CFCFA7", "#08172B"),
            bg="#08172B", width=20,
            text="AVAILABLE BOOKS",
            fg="#CFCFA7",
            font=("Georgia pro", 30, "bold")
        )
        self.books_redirect.grid(row=0, column=0)

        self.borrowed_books_redirect = tk.Button(
            custom_border(self.frame1, 2, 2, 10, 80, "#CFCFA7", "#08172B"),
            bg="#08172B",
            text="BORROWED BOOKS", fg="#CFCFA7",
            width=20,
            font=("Georgia pro", 30, "bold")
        )
        self.borrowed_books_redirect.grid(row=0, column=0)

        self.customer_list_redirect = tk.Button(
            custom_border(self.frame1, 3, 2, 10, 80, "#CFCFA7", "#08172B"),
            bg="#08172B", width=20,
            text="CUSTOMERS LIST",
            fg="#CFCFA7",
            font=("Georgia pro", 30, "bold"),
            command=self.customer_list
        )
        self.customer_list_redirect.grid(row=0, column=0)

        self.frame2 = tk.Frame(self, bg="black", height=self.winfo_height(), width=510)
        self.frame2.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.frame2.grid_propagate(False)
        self.frame2.grid_columnconfigure(0, weight=1)

        self.add_book_redirect = tk.Button(
            custom_border(self.frame2, 0, 0, (100, 10), color="white", bg_color="black"),
            text="ADD \nBOOK", width=20, height=5, command=self.add_book,
            background="black", fg="white",
            font=("Georgia pro", 20, "bold"))
        self.add_book_redirect.grid(row=0, column=0)

        self.add_user_redirect = tk.Button(
            custom_border(self.frame2, 1, 0, 5, color="white", bg_color="black"),
            text="ADD \nUSER", width=20, height=5,
            background="black", fg="white", font=("Georgia pro", 20, "bold")
        )
        self.add_user_redirect.grid(row=0, column=0)
        self.borrow_book_redirect = tk.Button(
            custom_border(self.frame2, 2, 0, 5, color="white", bg_color="black"),
            text="BORROW \nBOOK", width=20, height=5,
            background="black", fg="white", font=("Georgia pro", 20, "bold")
        )
        self.borrow_book_redirect.grid(row=0, column=0)

        self.return_book_redirect = tk.Button(
            custom_border(self.frame2, 3, 0, 5, color="white", bg_color="black"),
            text="RETURN \nBOOK", width=20, height=5,
            background="black", fg="white", font=("Georgia pro", 20, "bold")
        )
        self.return_book_redirect.grid(row=0, column=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.bind("<Configure>", self.on_window_resize)
        # self.load_books()

    def on_window_resize(self, event):
        window_height = self.winfo_height()
        window_width = self.winfo_width()
        self.frame1.configure(height=window_height, width=window_width * 66 / 100)
        self.frame2.configure(height=window_height, width=window_width * 34 / 100)

    def go_to_main_menu(self):
        self.frame1.grid()
        self.frame2.grid()
        self.customer_frame.grid_remove()

    def customer_list(self):
        self.frame1.grid_remove()
        self.frame2.grid_remove()

        self.customer_frame = tk.Frame(self, bg="#08172B", height=self.winfo_height(), width=1500)
        self.customer_frame.pack(fill="both", expand=True)
        self.customer_frame.grid_propagate(False)
        self.customer_frame.columnconfigure(0, weight=1)

        white_bar = tk.Frame(self.customer_frame, bg="white", width=5, height=self.winfo_height())
        white_bar.pack(fill="y", side="left", padx=30)
        customer_label = tk.Label(
            self.customer_frame, text="CUSTOMER LIST", font=("Georgia pro", 100), bg="#08172B", fg="#CFCFA7"
        )
        customer_label.grid(row=0, column=1, padx=(0, 80), pady=(60, 0))
        back_button = tk.Button(
            self.customer_frame, text='<', command=self.go_to_main_menu, height=5, bg="#08172B", fg="#CFCFA7", bd=0
        )
        back_button.grid(row=0, column=0, pady=(50, 0))

    def add_book(self):
        call_back = rejestbook.add_book(read_csv, self.entry_author.get(), self.entry_title.get(),
                                        int(self.entry_pages.get()))
        if call_back['type'] == 'error':
            messagebox.showerror("Error", call_back['message'])
        else:
            messagebox.showinfo("Success", call_back['message'])
            self.load_books()

    def load_books(self):
        df = read_csv("Library/book.csv",
                      'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
        if type(df) is not pd.DataFrame:
            return 0

        for index, row in df.iterrows():
            author, title = row['AUTHOR'], row['TITLE']
            for book in self.books:
                if author in book and title in book:
                    return 0
            pages, created = row['PAGES'], row['CREATED']
            updated, borrowed = row['UPDATED'], row['BORROWED']
            self.books.append((author, title, pages, created, updated, borrowed))
            self.listbox_author.insert(tk.END, f'{author}')
            self.listbox_title.insert(tk.END, f'{title}')
            self.listbox_pages.insert(tk.END, f'{pages}')
            self.listbox_created.insert(tk.END, f'{created}')
            self.listbox_updated.insert(tk.END, f'{updated}')
            if borrowed:
                self.listbox_borrowed.insert(tk.END, f'Tak')
            else:
                self.listbox_borrowed.insert(tk.END, f'Na stanie')

    def delete_book(self):
        try:
            book_id = int(self.remove_id.get())
        except ValueError as e:
            return e
        rejestbook.delete_book(read_csv, book_id=book_id)
        self.load_books()

    def edit_book(self):
        try:
            book_id = int(self.update_id.get())
            pages = int(self.update_pages.get())
        except ValueError as e:
            return e
        author = self.update_author.get()
        title = self.update_title.get()
        rejestbook.update_book(read_csv, book_id, author, title, pages)

    def add_customer(self):
        first_name, last_name = self.add_customer_first_name.get(), self.add_customer_last_name.get()
        email = self.add_customer_email.get()
        phone_number = self.add_customer_phone.get()
        street = self.add_customer_street.get()
        city = self.add_customer_city.get()
        country = self.add_customer_country.get()
        customerservice.add_customer(first_name, last_name, email, phone_number, street, city, country)
        pass

    def edit_customer(self):
        customer_id = self.update_customer_id.get()
        first_name = self.update_customer_first_name.get()
        last_name = self.update_customer_last_name.get()
        email = self.update_customer_email.get()
        phone_number = self.update_customer_phone.get()
        street = self.update_customer_street.get()
        city = self.update_customer_city.get()
        country = self.update_customer_country.get()
        customerservice.update_user(customer_id, f'{first_name} {last_name}',
                                    email, phone_number, street, city, country)

    def borrow_books(self):
        customer_id = self.borrow_book_id.get()
        args = self.borrow_book_titles.get()
        customerservice.borrow_book(customer_id, args)

    def return_books(self):
        customer_id = self.return_book_id.get()
        book_title = self.return_book_title.get()
        customerservice.return_book(customer_id, book_title)

    def delete_customer(self):
        pass


def main():
    return LibraryApp()


if __name__ == '__main__':
    main().mainloop()
