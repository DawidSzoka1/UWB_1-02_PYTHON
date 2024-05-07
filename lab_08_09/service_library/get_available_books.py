import pandas as pd


def get_available_books():
    df = pd.read_csv("Library/book.csv", usecols=['AUTHOR', 'TITLE', 'PAGES', 'BORROWED'])
    return df[df['BORROWED'] == False]
