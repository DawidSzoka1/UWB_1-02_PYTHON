"""
NAME
    rejestbook
DESCRIPTION
    This module provides functions to add book to database giving function to read_csv file,
    title of the book, author of the book and how many pages that book have.

"""
from datetime import date


def add_book(read_func, title, author, pages):
    """
    Add a book to the book.csv
    Args:
        read_func(function): outer function to read csv:
        title(str): title of the book:
        author(str): author of the book:
        pages(int): number of pages of the book:

    Returns:
        1 if book was successfully added else 0
    Raises:
        ValueError: if index of dataframe is not a number

    """
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    time = date.today()
    try:
        max_index = int(df.index[-1]) + 1
    except ValueError as e:
        return e
    df.loc[max_index] = [title.title(), author.title(), pages, time, time]
    if not df[max_index].empty:
        df.to_csv('Library/book.csv')
        print('Added book to database')
        return 1
    print('There was an error')
    return 0


def update_book(read_func, book_id, title, author, pages):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    time = date.today()
    if book_id in list(df.index.values):
        df.loc[book_id] = [title.title(), author.title(), pages, df.loc[book_id]['CREATED'], time]
        df.to_csv('Library/book.csv')
        print("Updated book")
        return 1
    print('Book not found')
    return 0


def delete_book(read_func, book_id=False, title=''):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED')
    if title:
        if df[df.TITLE == title.title()].empty:
            return 0
        df.drop(df[df.TITLE == title].index, inplace=True)
        df.to_csv('Library/book.csv')
        return 1
    elif book_id:
        if book_id not in list(df.index.values):
            return 0
        df.drop([book_id], inplace=True)
        df.to_csv('Library/book.csv')
        return 1
    return 0
