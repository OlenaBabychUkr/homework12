#
#Write a decorator that wraps a function in a try-except block 
#and prints an error if any type of error has happened. Example:

exists_dict = {'key': 'bar'}

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as error1:
            print(error1)
        except ValueError as error2:
            print(error2)
        except TypeError as error3:
            print(error3)
        except Exception:
            print('another error')
    return wrapper

@catch_errors
def some_function_with_risky_operation(data: dict):
    k = list(data.keys())[0]
    if k in exists_dict:
        print(exists_dict.get(k))
    else:
        print(f'KeyError no such key as {k}')


some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
