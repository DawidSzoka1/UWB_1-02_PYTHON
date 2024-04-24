from additionalfun import *
from datetime import date


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
    if not name or not customer_id:
        return 0
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if name.title() in df['NAME']:
        index = df['NAME'].index
        del df[df['NAME'] == name.title()]
        del df_address[index]
    elif customer_id in list(df.index.values):
        df.drop([customer_id], inplace=True)
        df_address.drop([customer_id], inplace=True)
    if df[df['ID'] == customer_id].empty or df[df['NAME'] == name].empty:
        df.to_csv('Library/customer.csv')
        df_address.to_csv('Library/address.csv')
        return 1

    return 0


def add_customer(name, email=None, phone_number=None, street=None, city=None, country=None):
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
    max_index = int(df.index[-1]) + 1
    max_index_address = int(df_address.index[-1]) + 1
    if max_index != max_index_address:
        return 0
    df_address.loc[max_index] = [street.title(), city.title(), country]
    df.loc[max_index] = [name.title(), email, phone_number, time, time]
    if df_address[max_index].empty or df[max_index].empty:
        delete_user(customer_id=max_index)
        return 0
    df.to_csv('Library/customer.csv')
    df_address.to_csv('Library/address.csv')
    return 1


def borrow_book():
    pass


def update_user(customer_id, name='', email='', phone_number=0, street='', city='', country=''):
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    df_address = read_csv('Library/address.csv',
                          'ID', 'STREET', 'CITY', 'COUNTRY')
    if customer_id not in list(df.index.values):
        print('NIe ma takiego uzytkownika')
        return 0
    elif customer_id not in list(df_address.index.values):
        print('Nie ma takiego adresu')
        return 0
    if update_customer(customer_id, df, name, email, phone_number):
        if update_address(customer_id, df_address, street, city, country):
            return 1
        print('Zmieniono tylko uzytkownika')
        return 1
    return 0
