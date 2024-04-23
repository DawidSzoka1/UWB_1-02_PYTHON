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
    else:
        print('Book not found')


def delete_book(read_func, book_id=False, title=False):
    df = read_func('Library/book.csv',
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
