from datetime import date
import os
from additionalfun import *
import pandas as pd
from pandas.errors import SettingWithCopyWarning, IndexingError


def update_address(customer_id, df_address, street='', city='', country=''):
    return_div = {'type': 'error'}
    if type(df_address) is not pd.DataFrame:
        return_div['message'] = f'df_address must be a Pandas dataframe not {type(df_address)}'
        return return_div
    if customer_id not in df_address.index:
        return_div['message'] = 'The customer does not exist'
        return return_div
    address = df_address.loc[customer_id]
    street = street.title() if street else address['STREET']
    city = city.title() if city else address['CITY']
    country = country if country else address['COUNTRY']
    try:
        df_address.loc[customer_id] = [street.title(), city.title(), country]
        df_address.to_csv('Library/address.csv')
        return_div['type'] = 'success'
        return_div['message'] = 'Successfully updated address'
        return return_div
    except ValueError as e:
        return_div['message'] = f'Value error while updating address {e}'
    except TypeError as e:
        return_div['message'] = f'Type error while updating address {e}'
    except SettingWithCopyWarning as e:
        return_div['message'] = f'SettingWithCopyWarning error while updating address {e}'
    except IndexingError as e:
        return_div['message'] = f'IndexingError error while updating address {e}'
    return return_div


def update_customer(customer_id, df, name='', email='', phone_number=0):
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'df_address must be a Pandas dataframe not {type(df)}'
        return return_div
    if customer_id not in df.index.values:
        return_div['message'] = 'Customer ID does not exist'
        return return_div
    user = df.loc[customer_id]
    name = name.title() if name else user['NAME']
    email = email if email else user['E-MAIL']
    phone_number = phone_number if phone_number else user['PHONE']
    try:
        df.loc[customer_id] = [name.title(), email, phone_number, df.loc[customer_id]['CREATE'], date.today()]
        df.to_csv('Library/customer.csv')
        return_div['type'] = 'success'
        return_div['message'] = 'Successfully updated user info'
        return return_div
    except ValueError as e:
        return_div['message'] = f'Value error while updating address {e}'
    except TypeError as e:
        return_div['message'] = f'Type error while updating address {e}'
    except SettingWithCopyWarning as e:
        return_div['message'] = f'SettingWithCopyWarning error while updating address {e}'
    except IndexingError as e:
        return_div['message'] = f'IndexingError error while updating address {e}'
    return return_div


def create_dataset():
    return_div = {'type': 'error'}
    if not os.path.exists('DATASET'):
        try:
            os.mkdir('DATASET')
            return_div['type'] = 'success'
            return_div['message'] = 'Successfully created DATABASE'
            return return_div
        except PermissionError as e:
            return_div['message'] = f'PermissionError {e}'
        except OSError as e:
            return_div['message'] = f'OSError {e}'
        return return_div
    if os.path.isdir('DATASET'):
        return_div['type'] = 'success'
        return_div['message'] = 'Dataset already exists'
        return return_div


def create_user_dataset(customer_id):
    return_div = {'type': 'error'}
    path = os.path.join(os.getcwd(), 'DATASET')
    if not os.path.exists('DATASET'):
        create = create_dataset()
        if create['type'] == 'error':
            return create
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'error with database: \n {df}'
        return return_div
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
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    path = os.path.join(os.getcwd(), 'DATASET')
    if type(df) is not pd.DataFrame:
        return 0
    elif customer_id not in df.index:
        print('No such customer')
        return 0
    elif os.path.exists(os.path.join(path, f'{customer_id}.txt')):
        return 0
    with open(os.path.join(path, f'{customer_id}.txt'), 'w') as f:
        pass
    return 1


def borrow_book_function(df_book, customer_id, title):
    return_div = {'type': 'error'}
    if type(df_book) is not pd.DataFrame:
        return_div['message'] = 'df_book is not a DataFrame'
        return return_div
    path = os.path.join(os.getcwd(), 'DATASET')
    if not os.path.exists(path):
        pass
    try:
        book_id = df_book[df_book['TITLE'] == title.title()].index[0]
    except IndexError:
        return_div['message'] = f'Book not found {title}'
        return return_div
    book = df_book.loc[book_id]
    if book['BORROWED']:
        return_div['message'] = f'Book is already borrowed {book["TITLE"]}'
        return return_div
    df_book.at[book_id, 'BORROWED'] = True
    df_book.to_csv('Library/book.csv')
    with open(os.path.join(path, f'{customer_id}.txt'), 'a') as f:
        f.write(
            f"id:{book_id}, author:{book['AUTHOR']},  title:{book['TITLE']},  "
            f"pages:{book['PAGES']}, borrowed: {date.today()}, returned: False\n")
    return_div['type'] = 'success'
    return return_div
