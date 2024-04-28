from datetime import date
import os
from additionalfun import *
import pandas as pd
from pandas.errors import SettingWithCopyWarning, IndexingError


def update_address(customer_id, df_address, street='', city='', country=''):
    if type(df_address) is not pd.DataFrame:
        print('df_address is not a Pandas DataFrame')
        return 0
    if customer_id not in df_address.index:
        print('customer_id is not in df_address')
        return 0
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


def create_user_dataset(customer_id):
    path = os.path.join(os.getcwd(), 'DATASET')
    if not os.path.exists('DATASET'):
        try:
            os.mkdir(path)
        except PermissionError as e:
            print('Error ', e)
            return 0
        except OSError as e:
            print('Error ', e)
            return 0
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    if not df:
        return 0
    elif customer_id not in df.index:
        print('No such customer')
        return 0
    elif os.path.exists(os.path.join(path, f'{customer_id}.txt')):
        return 1
    with open(os.path.join(path, f'{customer_id}.txt'), 'w') as f:
        pass
    return 1


def check_if_dataset(customer_id):
    if not os.path.exists('DATASET'):
        return create_user_dataset(customer_id)
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    path = os.path.join(os.getcwd(), 'DATASET')
    if not df:
        return 0
    elif customer_id not in df.index:
        print('No such customer')
        return 0
    elif not os.path.exists(os.path.join(path, f'{customer_id}.txt')):
        with open(os.path.join(path, f'{customer_id}.txt'), 'w') as f:
            pass
    return 1
