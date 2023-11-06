#
#Write a decorator that wraps a function in a try-except block 
#and prints an error if any type of error has happened. Example:

exists_dict = {'key': 'bar'}

def catch_errors(func):
    def wrapper(data):
        try:
            func(data)
        except Exception as e:
            print(f'An error occurred during execution of your function: {e}')
    return wrapper

@catch_errors
def some_function_with_risky_operation(data: dict):
    k = list(data.keys())[0]
    print(exists_dict.get(k))



some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})
