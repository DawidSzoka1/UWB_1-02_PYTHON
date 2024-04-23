from additionalfun import *
from datetime import date


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
        delete_customer(customer_id=max_index)
        return 0
    df.to_csv('Library/customer.csv')
    df_address.to_csv('Library/address.csv')
    return 1


def borrow_book():
    pass


def update_customer(name, email, phone_number):
    pass


def delete_customer(name='', customer_id=None):
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

    df.to_csv('Library/customer.csv')
    return 1
