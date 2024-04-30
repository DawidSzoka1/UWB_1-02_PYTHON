import pandas as pd


def read_csv(path_to_csv_file, *args):
    if 'ID' not in args:
        return 'ID is required in args'
    try:
        return pd.read_csv(
            path_to_csv_file,
            usecols=[*args],
            index_col='ID'
        )
    except FileNotFoundError as e:
        return f"File not found error occurred: {e}"
    except ValueError as e:
        return f"Value error occurred: {e}"
    except TypeError as e:
        return f"Type error occurred: {e}"
