def decorator(func):
    def wrapper(customer_id, *args):
        check = list(map(lambda title: func(customer_id, title), args))
        return 1 if all(check) else 0
    return wrapper
