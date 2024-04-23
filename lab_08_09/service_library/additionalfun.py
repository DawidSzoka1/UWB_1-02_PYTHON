import pandas as pd


def read_csv(path_to_csv_file, *args):
    if 'ID' not in args:
        try:
            return pd.read_csv(path_to_csv_file, usecols=[*args])
        except FileNotFoundError as e:
            print(f"File not found error occurred: {e}")
            return e
        except ValueError as e:
            print(f"Value error occurred: {e}")
            return e
    try:
        return pd.read_csv(
            path_to_csv_file,
            usecols=[*args],
            index_col='ID'
        )
    except FileNotFoundError as e:
        print(f"File not found error occurred: {e}")
        return e
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return e
