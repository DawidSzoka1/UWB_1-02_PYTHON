import pandas as pd


def read_csv(path_to_csv_file, *args):
    if 'ID' not in args:
        print('ID is required in args')
        return 0
    try:
        return pd.read_csv(
            path_to_csv_file,
            usecols=[*args],
            index_col='ID'
        )
    except FileNotFoundError as e:
        print(f"File not found error occurred: {e}")
        return 0
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return 0
    except TypeError as e:
        print('Type error occurred: ', e)
        return 0
