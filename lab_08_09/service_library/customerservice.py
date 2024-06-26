"""
NAME
    customerservice
DESCRIPTION
    This module allows the user to register a new user with address, delete user and update user info
    saving changes to csv file, borrow books from book.csv and return them

    This script requires pandas to be installed

FUNCTIONS
    This module contains the following functions:
    * add_customer(first_name, last_name, email='NO DATA', phone_number=None, street='NO DATA', city='NO DATA',
                 country='NO DATA')-
        Returns 1 if successful added customer to database, otherwise returns 0
    * update_user(customer_id, name='', email='', phone_number=0, street='', city='', country='')-
        Returns 1 if successful updated user info, otherwise returns 0
    * delete_user(name='', customer_id=None)-
        Returns 1 if successful deleted user and user address form database, otherwise returns 0
    * borrow_book(customer_id, *args)-
        Args:
            titles of books you want to borrow
        Returns 1 if successful borrowed book by user of books, otherwise returns 0
    * return_book(customer_id, book_title='')-
        Returns 1 if successful returned book to library, otherwise returns 0

Examples
    add_customer('Tomasz', 'Nowak', email='emaile@gmail.com', phone_number=4324324,
                  street='street', city='city', country='country')
    update_user(203, name='full name', email='em@gmail.com', phone_number=0, street='', city='', country='')
    delete_user(name='Tomasz Nowak') or delete_user(customer_id=203)
    borrow_book(203, 'tytul1', 'tytul2', ...)
    return_book(203, 'tytul1')
"""
from additionaluserfun import *
from decorator import decorator
from additionalfun import find_free_id
import pandas as pd
from datetime import datetime


def delete_user(name='', customer_id=None):
    """
    deleting a customer in customer.csv and in address.csv
    Args:
        name(str): The name of the customer:
        customer_id(int): The id of the customer:

    Returns:
       {'type': 'success', 'message': 'User was successfully deleted'} if user was successfully deleted else
        {'type': 'error', 'message': 'some error info'}
    Raises:
        TypeError: if customer_id is not a number

    """
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Error while reading database: \n {df}'
        return return_div
    try:
        customer_id = int(customer_id) if customer_id else df[df['NAME'] == name.title()].index[0]
    except IndexError:
        return_div['message'] = f'User with that name does not exist'
        return return_div
    except ValueError:
        return_div['message'] = f'ID must be int'
        return return_div
    except TypeError:
        return_div['message'] = f'ID must be int'
        return return_div
    print(customer_id)
    if customer_id not in list(df.index.values):
        return_div['message'] = f'No customer with that id'
        return return_div
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if type(df_address) is not pd.DataFrame:
        return_div['message'] = f'Error while reading database: \n {df_address}'
        return return_div
    try:
        df.drop([customer_id], inplace=True)
        df_address.drop([customer_id], inplace=True)
    except TypeError as e:
        return_div['message'] = f'Error while deleting user: \n {e}'
        return return_div
    except KeyError as e:
        return_div['message'] = f'Error while deleting user: \n {e}'
        return return_div
    df.to_csv('Library/customer.csv')
    df_address.to_csv('Library/address.csv')
    return_div['type'] = 'success'
    return_div['message'] = 'User was successfully deleted'
    return return_div


def add_customer(name, email='NO DATA', phone_number=None, street='NO DATA', city='NO DATA',
                 country='NO DATA'):
    """
    Function to add a customer to an existing csv file (customer.csv) with
    first name, last name , email ,phone number, data of created and updated customer

    Args:
        name(str): name of the customer:
        email(str): The email of the customer:
        phone_number(float): The phone number of the customer:
        street(str): The street of the customer:
        city(str): The city of the customer:
        country(str): The country of the customer:

    Returns:
        {'type': 'success', 'message': 'User was successfully created'} if user was successfully created else
        {'type': 'error', 'message': some_error_info}
    Exceptions:
        ValueError: If we try to add a customer with an invalid data value of all fields
        TypeError: If we try to add a customer with an invalid data type of all fields
        SettingWithCopyWarning: If we are working with copy of a dataframe
        IndexingError: If we try to go the wrong index
    """
    if name == '':
        return {'type': 'error', 'message': 'Name cannot be empty'}
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Error while loading the csv (customer.csv): {df}'
        return return_div
    try:
        if phone_number:
            phone_number = float(phone_number)
    except ValueError:
        return_div['message'] = f'phone number must be a number: {phone_number}'
        return return_div
    if f'{name.title()}' in df['NAME'].values and (email == 'NO DATA' or email == ''):
        return_div['message'] = f'You need to provide email because your first name and last name is taken'
        return return_div
    time = date.today()
    if phone_number in df['PHONE'].values and phone_number:
        return_div['message'] = 'Phone number is taken already'
        return return_div
    if email in df['E-MAIL'].values and email != 'NO DATA':
        return_div['message'] = 'E-mail is already taken already'
        return return_div
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if type(df_address) is not pd.DataFrame:
        return_div['message'] = f'Error while loading the csv (address.csv): {df}'
        return return_div

    next_id = find_free_id(df)
    try:
        df_address.loc[next_id] = [street.title(), city.title(), country]
        df.loc[next_id] = [name.title(), email, phone_number, time, time]
        df.to_csv('Library/customer.csv')
        df_address.to_csv('Library/address.csv')
        check_dataset = create_user_dataset(next_id)
        if check_dataset['type'] == 'error':
            delete_user(next_id)
            return check_dataset
        return_div['type'] = 'success'
        return_div['message'] = 'User was successfully created'
        return return_div
    except ValueError as e:
        return_div['message'] = f'ValueError: {e}'
    except TypeError as e:
        return_div['message'] = f'TypeError: {e}'
    except SettingWithCopyWarning as e:
        return_div['message'] = f'SettingWithCopyWarning: {e}'
    except IndexingError as e:
        return_div['message'] = f'IndexingError: {e}'
    return return_div


def borrow_book(customer_id, *args):
    return_div = {'type': 'error'}
    try:
        customer_id = int(customer_id)
    except ValueError:
        return_div['message'] = 'ID must be an integer'
        return return_div
    except TypeError:
        return_div['message'] = 'ID must be an integer'
        return return_div
    df_customer = read_csv('Library/customer.csv',
                           'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    if customer_id not in df_customer.index.values:
        return_div['message'] = 'There is no customer with that ID'
        return return_div
    if not args:
        return_div['message'] = 'You must provide some book titles'
        return return_div
    user_dataset = check_if_user_dataset(customer_id)
    if user_dataset['type'] == 'error':
        return user_dataset
    df_book = read_csv('Library/book.csv',
                       'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    if type(df_book) is not pd.DataFrame:
        return_div['message'] = f'Some error with database: \n {df_book}'
        return return_div
    borrowed_books_info = list(map(lambda title: borrow_book_function(df_book, customer_id, title), args))
    all_success = all(item['type'] == 'success' for item in borrowed_books_info)
    if not all_success:
        error_messages = list(filter(lambda text: text != '',
                                     [item['message'] if item['type'] == 'error' else '' for item in
                                      borrowed_books_info]))
        success = len(args) - len(error_messages)
        return_div['message'] = (f'Successfully borrowed ({success if success >= 0 else 0}),\n'
                                 f'Some error with borrowing books({len(error_messages)}):'
                                 f' {", ".join(error_messages)}')
        return return_div
    return_div['type'] = 'success'
    return_div['message'] = 'All books borrowed'
    return return_div


@decorator
def return_book(customer_id, book_title=''):
    return_div = {'type': 'error'}
    try:
        customer_id = int(customer_id)
    except ValueError:
        return_div['message'] = 'ID must be an integer'
        return return_div
    except TypeError:
        return_div['message'] = 'ID must be an integer'
        return return_div
    dataset = check_if_user_dataset(customer_id)
    if dataset['type'] == 'error':
        return dataset
    df_book = read_csv('Library/book.csv',
                       'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    if type(df_book) is not pd.DataFrame:
        return_div['message'] = f'Error with dataframe: {df_book}'
        return return_div
    try:
        book_id = df_book[df_book['TITLE'] == book_title.title()].index.values[0]
    except IndexError:
        return_div['message'] = f'Our library does not have that book title({book_title}).'
        return return_div
    if not book_id:
        return_div['message'] = 'Our library does not have that book title({book_title}).'
        return return_div

    path = os.path.join(os.getcwd(), 'DATASET')
    index = None
    with open(os.path.join(path, f'{customer_id}.txt'), 'r') as f:
        lines = f.readlines()
    late = False
    for i, line in enumerate(lines):
        if book_title.title() in line and 'False' in line:
            deadline = datetime.strptime(line.split(',')[-1].split(':')[1][:-1].strip(), '%Y-%m-%d').date()
            if deadline < date.today():
                late_days = deadline - date.today()
                return_div['message'] = (f'Your deadline to return the book was {late_days} ago,'
                                         f' you have to pay {late_days * 10} zl')
                return return_div
            index = i
            break
    if index is not None:
        lines[index] = lines[index].replace('returned: False', f'returned: {date.today()}')
        with open(os.path.join(path, f'{customer_id}.txt'), 'w') as file:
            file.writelines(lines)
        df_book.at[book_id, 'BORROWED'] = False
        df_book.to_csv('Library/book.csv')
        return_div['type'] = 'success'
        return_div['message'] = f'Successfully returned book ({book_title})'
        return return_div
    return_div['message'] = f'The book was already returned or you do not borrowed that book ({book_title})'
    return return_div


def update_user(customer_id, name='', email='', phone_number=0, street='', city='', country=''):
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame or type(df_address) is not pd.DataFrame:
        return_div['message'] = (f'Error while reading dataframe: \n '
                                 f'{df if type(df) is not pd.DataFrame else df_address}')
        return return_div
    if customer_id not in df.index.values:
        return_div['message'] = f'User with that id was not found'
        return return_div
    check_update_user = update_customer(customer_id, df, name, email, phone_number)
    check_update_address = update_address(customer_id, df_address, street, city, country)
    if check_update_user['type'] == 'success':
        return_div['type'] = 'success'
        return_div['message'] = 'Successfully updated user info'
        if check_update_address['type'] == 'success':
            return_div['message'] = 'Successfully updated both user info and user address'
        return_div['error_address'] = check_update_address['message']
        return return_div
    return_div['message'] = \
        (f'Some error occurred while updating data: \n'
         f'{check_update_user["message"] if check_update_user["type"] == "error" else "personal info was updated succesfully"}'
         f'\n{check_update_address["message"] if check_update_address["type"] == "error" else "address info was updated succesfully"}')
    return return_div
