import pandas as pd


def get_books(borrowed=False):
    df = pd.read_csv("Library/book.csv", usecols=['AUTHOR', 'TITLE', 'PAGES', 'BORROWED'])
    return df[df['BORROWED'] == borrowed]


def get_customers():
    df = pd.read_csv(
        "Library/customers.csv",
        usecols=['ID', 'NAME', 'E-MAIL', 'PHONE'],
        index_col='ID')
    df_address = pd.read_csv("Library/address.csv", index_col='ID')

    return df, df_address
