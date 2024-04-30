from customerservice import *
import rejestbook
import tkinter as tk


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System")

        self.books = []

        self.label_title = tk.Label(self, text="Title:")
        self.label_title.grid(row=0, column=0, padx=5, pady=5)
        self.entry_title = tk.Entry(self)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5)

        self.label_author = tk.Label(self, text="Author:")
        self.label_author.grid(row=1, column=0, padx=5, pady=5)
        self.entry_author = tk.Entry(self)
        self.entry_author.grid(row=1, column=1, padx=5, pady=5)

        self.label_pages = tk.Label(self, text="Pages:")
        self.label_pages.grid(row=2, column=0, padx=5, pady=5)
        self.entry_pages = tk.Entry(self)
        self.entry_pages.grid(row=2, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self, text="Add Book", command=self.add_book)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_books = tk.Listbox(self)
        self.listbox_books.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # self.button_remove = tk.Button(self, text="Remove Book", command=self.remove_book)
        # self.button_remove.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        #
        # self.load_books()

    def add_book(self):
        rejestbook.add_book(read_csv, self.entry_author.get(), self.entry_title.get(), int(self.entry_pages.get()))

    def load_books(self):
        self.listbox_books.delete(0, tk.END)
        self.books = []

        df = read_csv("books.csv",
                      'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
        for index, row in df.iterrows():
            author, title, pages, created = row['AUTHOR'], row['TITLE'], row['PAGES'], row['CREATED']
            updated, borrowed = row['UPDATED'], row['BORROWED']
            self.books.append((title, author))
            self.listbox_books.insert(tk.END, f"{title} by {author}")


def main():
    pass


if __name__ == '__main__':
    LibraryApp().mainloop()
    main()
