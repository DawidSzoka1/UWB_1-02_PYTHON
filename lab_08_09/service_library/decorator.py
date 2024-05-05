def decorator(func):
    def wrapper(customer_id, *args):
        return_div = {'type': 'error'}
        check = list(map(lambda title: func(customer_id, title), args))
        all_success = all(item['type'] == 'success' for item in check)
        if all_success:
            return_div['type'] = 'success'
            return_div['message'] = 'All books were successfully returned'
            return return_div
        error_messages = list(filter(lambda text: text != '',
                                         [item['message'] if item['type'] == 'error' else '' for item in
                                          check]))
        return_div['message'] = f'Some error with borrowing books: {", ".join(error_messages)}'
        return return_div
    return wrapper
