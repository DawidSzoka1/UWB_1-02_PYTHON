"""
NAME
    customerservice
DESCRIPTION
    This module allows the user to register a new user with address, delete user and update user info
    saving changes to csv file

    This script doesn't require any packages

FUNCTIONS
    This module contains the following functions:
    * add_customer(f(path_to_csv_file, *args), path_to_csv, title, author, pages)-
        Returns
    * update_user(f(path_to_csv_file, *args), path_to_csv, book_id, title, author, pages)-
        Returns
    * delete_user(f(path_to_csv_file, *args), path_to_csv, book_id=None, title='')-
        Returns

Examples
    add_customer()
    update_user()
    delete_user()
"""
from additionalfun import *
from datetime import date
import os
import random


def delete_user(name='', customer_id=None):
    """
    deleting a customer in customer.csv and in address.csv
    Args:
        name(str): The name of the customer:
        customer_id(int): The id of the customer:

    Returns:
        1 if successful, else 0

    """
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    if name:
        if name.title() not in df['NAME']:
            print('No customer with that name')
            return 0
    else:
        if customer_id not in df.index:
            print('No customer with that id')
            return 0
    customer_id = customer_id if customer_id else df[df['NAME'] == name.title()].index
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    try:
        df.drop([customer_id], inplace=True)
        df_address.drop([customer_id], inplace=True)
    except TypeError as e:
        print('TypeError', e)
        return 0
    if df.loc[customer_id].empty:
        df.to_csv('Library/customer.csv')
        df_address.to_csv('Library/address.csv')
        return 1

    return 0


def add_customer(name, email='', phone_number='', street='', city='', country=''):
    """
    Function to add a customer to an existing csv file (customer.csv) with
    name and email and phone number and data of created and updated customer

    Args:
        name(str): The name of the customer:
        email(str): The email of the customer:
        phone_number(str): The phone number of the customer:
        street(str): The street of the customer:
        city(str): The city of the customer:
        country(str): The country of the customer:

    Returns:
        1 if successful added customer to customer.csv and address to address.csv, else 0
    """
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    time = date.today()
    if phone_number in df['PHONE']:
        print('Phone number is already taken')
        return 0
    if email in df['E-MAIL']:
        print('E-mail is already taken')
        return 0
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if not df or not df_address:
        print('Problems with reading customer data or address data')
        return 0

    max_index = random.randint(1000, 9999)
    while max_index in df.index:
        max_index = random.randint(1000, 9999)
    try:
        df_address.loc[max_index] = [street.title(), city.title(), country]
        df.loc[max_index] = [name.title(), email, phone_number, time, time]
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


def borrow_book():
    pass


def return_book(customer_id):
    os.chdir('DATABASE')
    if customer_id not in os.listdir():
        print('There is no customer with that id')
        return 0
    with open(f'{customer_id}.txt', 'w'):
        pass


def update_user(customer_id, name='', email='', phone_number=0, street='', city='', country=''):
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if customer_id not in df.index:
        print('NIe ma takiego uzytkownika')
        return 0
    elif customer_id not in df_address.index:
        print('Nie ma takiego adresu')
        return 0
    if update_customer(customer_id, df, name, email, phone_number):
        if update_address(customer_id, df_address, street, city, country):
            print('Poprawnie zmieniono wszystkie dane')
            return 1
        print('Zmieniono tylko uzytkownika')
        return 1
    print('Wystapil problem ze zmiana uzytkownika')
    return 0
