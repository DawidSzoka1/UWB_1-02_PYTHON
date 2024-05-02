"""
NAME
    rejestbook
DESCRIPTION
    This module allows the user to add book update book and delete book from csv file
    book info: title, author, pages

    This script requires pandas to be installed

FUNCTIONS
    This module contains the following functions:
    * add_book(f(path_to_csv_file, *args), title, author, pages)-
        where f(path_to_csv_file, *args) is function to read_csv files using columns that came in args
        Returns 1 if successful, otherwise returns 0
    * update_book(f(path_to_csv_file, *args), book_id, author='', title_book='', pages=None)-
        where f(path_to_csv_file, *args) is function to read_csv files using columns that came in args
        Returns 1 if successful, otherwise returns 0
    * delete_book(f(path_to_csv_file, *args), book_id=None, title='')-
        where f(path_to_csv_file, *args) is function to read_csv files using columns that came in args
        Returns 1 if successful, otherwise returns 0

Examples
    add_book()
    update_book()
    delete_book()
"""
from datetime import date
import pandas as pd
from additionalfun import find_free_id


def add_book(read_func, author, title, pages):
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
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')

    if type(df) is not pd.DataFrame:
        return df
    time = date.today()
    next_id = find_free_id(df)
    df.loc[next_id] = [author.title(), title.title(), pages, time, time, False]
    if not df.loc[next_id].empty:
        df.to_csv('Library/book.csv')
        print('Added book to database')
        return 1
    print('There was an error')
    return 0


def update_book(read_func, book_id, author='', title_book='', pages=None):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    if type(df) is not pd.DataFrame:
        return df
    time = date.today()
    if book_id not in df.index:
        print('Book not found')
        return 0

    author = author.title() if author else df.loc[book_id]['AUTHOR']
    title_book = title_book.title() if title_book else df.loc[book_id]['TITLE']
    pages = pages if pages else df.loc[book_id]['PAGES']

    df.loc[book_id] = [author, title_book, pages, df.loc[book_id]['CREATED'], time, df.loc[book_id]['BORROWED']]
    df.to_csv('Library/book.csv')
    print("Updated book")
    return 1


def delete_book(read_func, book_id=None, title=''):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')

    if type(df) is not pd.DataFrame:
        return df
    if title:
        if df[df.TITLE == title.title()].empty:
            return 0
        df.drop(df[df.TITLE == title].index, inplace=True)
        df.to_csv('Library/book.csv')
        print('Successfully deleted book')
        return 1
    elif book_id:
        if book_id not in list(df.index.values):
            return 0
        df.drop(book_id, inplace=True)
        df.to_csv('Library/book.csv')
        print('Successfully deleted book')
        return 1
    return 0
