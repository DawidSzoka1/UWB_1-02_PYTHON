import pandas as pd
from datetime import date

from pandas.errors import SettingWithCopyWarning, IndexingError


def read_csv(path_to_csv_file, *args):
    if 'ID' not in args:
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


def update_address(customer_id, df_address, street='', city='', country=''):
    address = df_address.loc[customer_id]
    street = street.title() if street else address['STREET']
    city = city.title() if city else address['CITY']
    country = country if country else address['COUNTRY']
    try:
        df_address.loc[customer_id] = [street.title(), city.title(), country]
        df_address.to_csv('Library/address.csv')
        return 1
    except ValueError as e:
        print("Value error occurred: ", e)
        return 0
    except TypeError as e:
        print("Type error occurred: ", e)
        return 0
    except SettingWithCopyWarning as e:
        print("SettingWithCopyWarning error occurred: ", e)
        return 0
    except IndexingError as e:
        print("IndexingErrors error occurred: ", e)
        return 0


def update_customer(customer_id, df, name='', email='', phone_number=0):
    user = df.loc[customer_id]
    name = name.title() if name else user['NAME']
    email = email if email else user['E-MAIL']
    phone_number = phone_number if phone_number else user['PHONE']
    try:
        df.loc[customer_id] = [name.title(), email, phone_number, df.loc[customer_id]['CREATE'], date.today()]
        df.to_csv('Library/customer.csv')
        return 1
    except ValueError as e:
        print("Value error occurred: ", e)
        return 0
    except TypeError as e:
        print("Type error occurred: ", e)
        return 0
    except SettingWithCopyWarning as e:
        print("SettingWithCopyWarning error occurred: ", e)
        return 0
    except IndexingError as e:
        print("IndexingErrors error occurred: ", e)
        return 0
