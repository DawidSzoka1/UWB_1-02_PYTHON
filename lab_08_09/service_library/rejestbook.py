from additionalfun import *
from datetime import date


def add_book(book_id, title, author, pages):
    df = read_csv('book.csv',
                  'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    time = date.today()

    if book_id in list(df.index.values):
        return 'Book id is taken'
    df.loc[book_id] = [title.title(), author.title(), pages, time, time]
    df.to_csv('Library/book.csv')


def update_book(book_id, title, author, pages):
    df = read_csv('book.csv',
                  'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    time = date.today()
    if book_id in list(df.index.values):
        df.loc[book_id] = [title.title(), author.title(), pages, df.loc[book_id]['CREATED'], time]
        df.to_csv('Library/book.csv')
    else:
        print('Book not found')


def delete_book(book_id=0, title=''):
    df = read_csv('book.csv',
                  'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    if title:
        if not df[df.TITLE == title].empty:
            df.drop(df[df.TITLE == title].index, inplace=True)
            df.to_csv('Library/book.csv')
        else:
            return 'Book not found'
    elif book_id:
        if book_id not in list(df.index.values):
            return 'Book not found'
        df.drop([book_id], inplace=True)
        df.to_csv('Library/book.csv')
    else:
        return 'Book not found'
    return 'Book deleted'
