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
        success_amount = len(args) - len(error_messages)
        return_div['message'] = (f'Successfully returned ({success_amount if success_amount >= 0 else 0}),\n'
                                 f'Some error with returning books({len(error_messages)}):'
                                 f' {", ".join(error_messages)}')
        return return_div

    return wrapper
