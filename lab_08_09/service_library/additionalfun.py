import pandas as pd


def read_books(csv_file):
    return pd.read_csv(f'Library/{csv_file}',
                       usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'],
                       index_col='ID')
