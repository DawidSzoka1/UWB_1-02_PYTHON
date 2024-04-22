from additionalfun import *
from datetime import date


def add_book(book_id, title, author, pages):
    df = read_books('book.csv')
    time = date.today()

    if book_id in list(df.index.values):
        return 'Book id is taken'
    df.loc[book_id] = [title.title(), author.title(), pages, time, time]
    df.to_csv('Library/book.csv')


def update_book(book_id, title, author, pages):
    df = read_books('book.csv')
    time = date.today()
    if book_id in list(df.index.values):
        df.loc[book_id] = [title.title(), author.title(), pages, df.loc[book_id]['CREATED'], time]
        df.to_csv('Library/book.csv')
    else:
        print('Book not found')


def delete_book(book_id):
    df = read_books('book.csv')
    if book_id not in list(df.index.values):
        return 'Book not found'
    df.drop([103], inplace=True)
    df.to_csv('Library/book.csv')
    return 'Book deleted'


print(delete_book(103))
