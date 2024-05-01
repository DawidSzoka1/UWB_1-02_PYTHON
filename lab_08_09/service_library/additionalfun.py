import pandas as pd
import random


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


def find_free_id(df):
    def random_id():
        return random.randint(1000, 9999)

    def check_id(index):
        return index if index not in df.index else check_id(random_id())
    return check_id(random_id())
