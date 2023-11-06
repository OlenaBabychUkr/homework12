"""
Write a decorator that ensures a function is only called by users with a specific role. 
Each function should have an user_type with a string type in kwargs. 
"""

def is_admin(func):
    def wrapper (user_type: str):
        # Some very dangerous operation
        if user_type == 'admin':
            print(f'you can do everything')
            return func()
        else:
            print("Permission denied")
    return wrapper

@is_admin
def show_customer_receipt():
    print ("Some very dangerous operation")

show_customer_receipt(user_type='admin')
show_customer_receipt(user_type='user')
