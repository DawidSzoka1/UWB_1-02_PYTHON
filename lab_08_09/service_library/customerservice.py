from additionalfun import *
from datetime import date


def add_customer(name, email=None, phone_number=None):
    """
    Function to add a customer to an existing csv file (customer.csv) with
    name and email and phone number and data of created and updated customer

    Args:
        name(str): The name of the customer:
        email(str): The email of the customer:
        phone_number(str): The phone number of the customer:

    Returns:
        0 if the customer phone_number is already taken or email is already taken
        else 'Added Customer successfully'
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
    max_index = int(df.index[-1]) + 1
    df.loc[max_index] = [name.title(), email, phone_number, time, time]
    df.to_csv('Library/customer.csv')
    return 'Added Customer successfully'


def update_customer(name, email, phone_number):
    pass


def delete_customer(name):
    pass