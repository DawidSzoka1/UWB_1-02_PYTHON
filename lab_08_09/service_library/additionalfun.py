import pandas as pd


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
    if customer_id not in df_address.index:
        print('Customer ID not found')
        return 0
    address = df_address.loc[customer_id]
    street = street.title() if street else address['STREET']
    city = city.title() if city else address['CITY']
    country = country if country else address['COUNTRY']
    df_address.loc[customer_id] = [street.title(), city.title(), country]
    df_address.to_csv('Library/address.csv')
    return 1


def update_customer(customer_id, df, name='', email='', phone_number=0):
    if customer_id not in df.index:
        print('Customer ID not found')
        return 0
    user = df.loc[customer_id]
    name = name.title() if name else user['NAME']
    email = email if email else user['E-MAIL']
    phone_number = phone_number if phone_number else user['PHONE']
    df.loc[customer_id] = [name.title(), email, phone_number, df.loc[customer_id]['CREATE'], date.today()]
    df.to_csv('Library/customer.csv')
    return 1


def delete_address():
    pass


def delete_customer():
    pass
