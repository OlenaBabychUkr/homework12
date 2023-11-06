#
#Optional: Create a decorator that will check types. 
#It should take a function with arguments and validate inputs with annotations. 
#It should work for all possible functions. Don`t forget to check the return type as well


def check_types(func):
    def wrapper(a: int, b: int):
        if type(a) is int or type(b) is int:
            return(func(a,b))
        else:
            raise TypeError('incorrect types') 
    return wrapper

@check_types
def add(a: int, b: int) -> int:
    return a+b


add(1, 2)
add("1", "2")


