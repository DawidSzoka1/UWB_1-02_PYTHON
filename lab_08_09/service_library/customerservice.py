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
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Error while reading database: \n {df}'
        return return_div
    try:
        customer_id = customer_id if customer_id else df[df['NAME'] == name.title()].index[0]
    except IndexError:
        return_div['message'] = f'User with that name does not exist'
        return return_div
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
    if df.loc[customer_id].empty:
        df.to_csv('Library/customer.csv')
        df_address.to_csv('Library/address.csv')
        return_div['type'] = 'success'
        return_div['message'] = 'User was successfully deleted'
        return return_div
    return_div['message'] = 'Some unexpected error occurred'
    return return_div


def add_customer(first_name, last_name, email='NO DATA', phone_number=None, street='NO DATA', city='NO DATA',
                 country='NO DATA'):
    """
    Function to add a customer to an existing csv file (customer.csv) with
    first name, last name , email ,phone number, data of created and updated customer

    Args:
        first_name(str): First name of the customer:
        last_name(str): Last name of the customer:
        email(str): The email of the customer:
        phone_number(str): The phone number of the customer:
        street(str): The street of the customer:
        city(str): The city of the customer:
        country(str): The country of the customer:

    Returns:
        1 if successful added customer to customer.csv and address to address.csv, else 0
    Exceptions:
        ValueError: If we try to add a customer with an invalid data value of all fields
        TypeError: If we try to add a customer with an invalid data type of all fields
        SettingWithCopyWarning: If we are working with copy of a dataframe
        IndexingError: If we try to go the wrong index
    """
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    return_div = {'type': 'error'}
    if type(df) is not pd.DataFrame:
        return_div['message'] = f'Error while loading the csv (customer.csv): {df}'
        return return_div
    try:
        phone_number = float(phone_number)
    except ValueError:
        return_div['message'] = f'phone number must be a number: {phone_number}'
        return return_div
    time = date.today()
    if phone_number in df['PHONE'].values:
        return_div['message'] = 'Phone number is taken already'
        return return_div
    if email in df['E-MAIL'].values:
        return_div['message'] = 'E-mail is already taken already'
        return return_div
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if type(df_address) is not pd.DataFrame:
        return_div['message'] = f'Error while loading the csv (address.csv): {df}'
        return return_div

    next_id = find_free_id(df)
    name = f'{first_name.title()} {last_name.title()}'
    create_user_dataset(next_id)
    try:
        df_address.loc[next_id] = [street.title(), city.title(), country]
        df.loc[next_id] = [name.title(), email, phone_number, time, time]
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
    df.to_csv('Library/customer.csv')
    df_address.to_csv('Library/address.csv')
    return 1


def borrow_book(customer_id, *args):
    if not args:
        return 0
    if not check_if_dataset(customer_id):
        return 0
    df_book = read_csv('Library/book.csv',
                       'ID', 'AUTHOR', 'TITLE', 'PAGES', 'BORROWED')
    if type(df_book) is not pd.DataFrame:
        print('Enter a valid dataframe')
        return 0
    borrowed_books_info = list(map(lambda title: borrow_book_function(df_book, customer_id, title), args))
    return 1 if all(borrowed_books_info) else 0


@decorator
def return_book(customer_id, book_title=''):
    if not check_if_dataset(customer_id):
        return 0
    df_book = read_csv('Library/book.csv',
                       'ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'BORROWED')
    if type(df_book) is not pd.DataFrame:
        return 0
    try:
        book_id = df_book[df_book['TITLE'] == book_title.title()].index.values[0]
    except IndexError as e:
        print('Our library does not have that book title.')
        return 0
    if not book_id:
        print('Our library does not have that book title.')
        return 0

    path = os.path.join(os.getcwd(), 'DATASET')
    index = None
    with open(os.path.join(path, f'{customer_id}.txt'), 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.split(',')[2].split(':')[1] == book_title.title() and line.split(',')[5].split(':')[1][:-1].strip() == 'False':
            index = i
            break
    if index is not None:
        lines[index] = lines[index].replace('returned: False', f'returned: {date.today()}')
        with open(os.path.join(path, f'{customer_id}.txt'), 'w') as file:
            file.writelines(lines)
        df_book.at[book_id, 'BORROWED'] = False
        df_book.to_csv('Library/book.csv')
        print('Successfully returned book')
        return 1
    print('The book was not found in your database or you already returned the book')
    return 0


def update_user(customer_id, name='', email='', phone_number=0, street='', city='', country=''):
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED')
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if not df or not df_address:
        return 0
    if type(df) is not pd.DataFrame or type(df_address) is not pd.DataFrame:
        print('Please enter a valid dataframe')
        return 0
    if customer_id not in df.index:
        print('User does not exist')
        return 0
    elif customer_id not in df_address.index:
        print('Address does not exist')
        return 0
    if update_customer(customer_id, df, name, email, phone_number):
        if update_address(customer_id, df_address, street, city, country):
            print('Successfully updated')
            return 1
        print('Only user was updated')
        return 1
    return 0
