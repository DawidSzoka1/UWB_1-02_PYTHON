from customerservice import *
import rejestbook
import tkinter as tk


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System")
        self.geometry("1000x500")
        self.books = []

        # self.label_author = tk.Label(self, text="Author:")
        # self.label_author.grid(row=0, column=0, padx=5, pady=5)
        # self.entry_author = tk.Entry(self)
        # self.entry_author.grid(row=0, column=1, padx=5, pady=5)
        #
        # self.label_title = tk.Label(self, text="Title:")
        # self.label_title.grid(row=1, column=0, padx=5, pady=5)
        # self.entry_title = tk.Entry(self)
        # self.entry_title.grid(row=1, column=1, padx=5, pady=5)
        #
        # self.label_pages = tk.Label(self, text="Pages:")
        # self.label_pages.grid(row=2, column=0, padx=5, pady=5)
        # self.entry_pages = tk.Entry(self)
        # self.entry_pages.grid(row=2, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self, text="Add Book", command=self.add_book)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.label_listbox_author = tk.Label(self, text="Author")
        self.label_listbox_author.grid(row=0, column=0, pady=5, sticky="ew")

        self.label_listbox_title = tk.Label(self, text="Title")
        self.label_listbox_title.grid(row=0, column=1, pady=5, sticky="ew")

        self.label_listbox_pages = tk.Label(self, text="Pages")
        self.label_listbox_pages.grid(row=0, column=2, pady=5, sticky="ew")

        self.label_listbox_created = tk.Label(self, text="CREATED")
        self.label_listbox_created.grid(row=0, column=3, pady=5, sticky="ew")

        self.label_listbox_updated = tk.Label(self, text="UPDATED")
        self.label_listbox_updated.grid(row=0, column=4, pady=5, sticky="ew")

        self.label_listbox_borrowed = tk.Label(self, text="BORROWED")
        self.label_listbox_borrowed.grid(row=0, column=5, pady=5, sticky="ew")

        self.listbox_title = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_title.grid(row=1, column=0, columnspan=1, pady=10, sticky="nsew")

        self.listbox_author = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_author.grid(row=1, column=1, columnspan=1, pady=10, sticky="nsew")

        self.listbox_pages = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_pages.grid(row=1, column=2, columnspan=1, pady=10, sticky="nsew")

        self.listbox_created = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_created.grid(row=1, column=3, columnspan=1, pady=10, sticky="nsew")

        self.listbox_updated = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_updated.grid(row=1, column=4, columnspan=1, pady=10, sticky="nsew")

        self.listbox_borrowed = tk.Listbox(self, width=10, height=25, font=('Arial', 16))
        self.listbox_borrowed.grid(row=1, column=5, columnspan=1, pady=10, sticky="nsew")

        # self.button_remove = tk.Button(self, text="Remove Book", command=self.remove_book)
        # self.button_remove.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        #
        self.load_books()

    def add_book(self):
        rejestbook.add_book(read_csv, self.entry_author.get(), self.entry_title.get(), int(self.entry_pages.get()))
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
            self.listbox_borrowed.insert(tk.END, f'{borrowed}')


def main():
    pass


if __name__ == '__main__':
    LibraryApp().mainloop()
    main()
