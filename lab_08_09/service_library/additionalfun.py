import pandas as pd


def read_csv(csv_file, *args):
    return pd.read_csv(
        f'Library/{csv_file}',
        usecols=[*args],
        index_col='ID'
    )
