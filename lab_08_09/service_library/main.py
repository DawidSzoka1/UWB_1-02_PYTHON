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
        self.label_listbox_author.grid(row=0, column=0, padx=1, pady=5)

        self.label_listbox_title = tk.Label(self, text="Title")
        self.label_listbox_title.grid(row=0, column=1, padx=1, pady=5)

        self.label_listbox_pages = tk.Label(self, text="Pages")
        self.label_listbox_pages.grid(row=0, column=2, padx=1, pady=5)

        self.label_listbox_created = tk.Label(self, text="CREATED")
        self.label_listbox_created.grid(row=0, column=3, padx=1, pady=5)

        self.label_listbox_updated = tk.Label(self, text="UPDATED")
        self.label_listbox_updated.grid(row=0, column=4, padx=1, pady=5)

        self.label_listbox_borrowed = tk.Label(self, text="BORROWED")
        self.label_listbox_borrowed.grid(row=0, column=5, padx=1, pady=5)

        self.listbox_books = tk.Listbox(self, width=75, height=25, font=('Arial', 18))
        self.listbox_books.grid(row=1, column=0, columnspan=6, padx=5, pady=40)

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
            self.listbox_books.insert(tk.END, f"{df}")
            return 0

        for index, row in df.iterrows():
            author, title = row['AUTHOR'], row['TITLE']
            for book in self.books:
                if author in book and title in book:
                    return 0
            pages, created = row['PAGES'], row['CREATED']
            updated, borrowed = row['UPDATED'], row['BORROWED']
            self.books.append((author, title, pages, created, updated, borrowed))
            self.listbox_books.insert(tk.END, f"{author}, {title}, {pages}, {created}, {updated}, {borrowed}")


def main():
    pass


if __name__ == '__main__':
    LibraryApp().mainloop()
    main()
