from additionalfun import *
from datetime import date


def add_customer(name, email=None, phone_number=None):
    df = read_csv('Library/customer.csv',
                  'ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATE', 'UPDATE')
    time = date.today()
    if phone_number in df['PHONE']:
        print('Phone number is already taken')
        return 0
    if email in df['E-MAIL']:
        print('E-mail is already taken')
        return 0
    max_index = df.index[-1] + 1
    df.loc[max_index] = [name.title(), email, phone_number, time, time]
    df.to_csv('Library/customer.csv')
    print('Added customer')



def update_customer(name, email, phone_number):
    pass


def delete_customer(name):
    pass
