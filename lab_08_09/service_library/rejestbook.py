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
    add_book(read_csv, 'Author', 'Title', 304)
    update_book(read_csv, 201, 'new', 'newT', 321)
    delete_book(read_csv, book_id=201)
"""
from datetime import date
import pandas as pd
from additionalfun import find_free_id, read_csv


def add_book(read_func, author, title, pages):
    """
    Add a book to the book.csv
    Args:
        read_func(function): outer function to read csv:
        title(str): title of the book:
        author(str): author of the book:
        pages(int): number of pages of the book:

    Returns:
        {'type': 'success', 'message': 'Book was successfully added'} if book was successfully added else
        {'type': 'error', 'message': 'some error info'}
    Raises:
        ValueError: if index of dataframe is not a number and if pages is not int

    """
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Some error with database {df}'
        return return_div
    try:
        pages = int(pages)
    except ValueError:
        return_div['message'] = 'Pages must be a int'
        return return_div
    time = date.today()
    next_id = find_free_id(df)
    df.loc[next_id] = [author.title(), title.title(), pages, time, time, False]
    return_div['type'] = 'success'
    return_div['message'] = 'Book was successfully added'
    if df.loc[next_id].empty:
        return_div['type'] = 'error'
        return_div['message'] = 'some error occurred'
    df.to_csv('Library/book.csv')
    return return_div


def update_book(read_func, book_id, author='', title_book='', pages=None):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Some error with database {df}'
        return return_div
    time = date.today()
    if book_id not in df.index:
        return_div['message'] = 'Book not found'
        return return_div
    author = author.title() if author else df.loc[book_id]['AUTHOR']
    title_book = title_book.title() if title_book else df.loc[book_id]['TITLE']
    pages = pages if pages else df.loc[book_id]['PAGES']
    df.loc[book_id] = [author, title_book, pages, df.loc[book_id]['CREATED'], time, df.loc[book_id]['BORROWED']]
    df.to_csv('Library/book.csv')
    return_div['type'] = 'success'
    return_div['message'] = 'Book was updated successfully'
    return return_div


def delete_book(read_func, book_id=None, title=''):
    df = read_func('Library/book.csv',
                   'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    return_div = {'type': 'error'}

    if type(df) is not pd.DataFrame:
        return_div['message'] = f'There was an error with loading database:\n {df}'
        return return_div
    try:
        book_id = book_id if book_id else df[df['TITLE'] == title.title()].index[0]
    except IndexError:
        return_div['message'] = f'Book with title {title.title()} does not exist'
        return return_div
    if book_id not in list(df.index.values):
        return_div['message'] = 'Book with that id does not exist'
        return return_div
    return_div['message'] = 'Book was deleted successfully'
    return_div['type'] = 'success'
    df.drop(book_id, inplace=True)
    df.to_csv('Library/book.csv')
    return return_div
