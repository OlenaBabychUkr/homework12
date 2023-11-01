#
#Write a decorator that wraps a function in a try-except block 
#and prints an error if any type of error has happened. Example:

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exp:
            print(exp, exp.__traceback__)
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    if 'key' in data:
        print(data['key'])
    else:
        print('The data dictionary does not contain a `key` key.')


some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
