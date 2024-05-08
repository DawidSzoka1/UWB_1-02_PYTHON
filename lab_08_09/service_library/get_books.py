import pandas as pd


def get_books(borrowed=False):
    df = pd.read_csv("Library/book.csv", usecols=['AUTHOR', 'TITLE', 'PAGES', 'BORROWED'])
    return df[df['BORROWED'] == borrowed]
