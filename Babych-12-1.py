#
#Write a decorator that ensures a function is only called by users with a specific role. 
#Each function should have an user_type with a string type in kwargs. 

def is_admin(func):
    def show_customer_receipt(user_type: str):
        # Some very dangerous operation
        if user_type == 'user':
            raise ValueError("Permission denied")
        elif user_type == 'admin':
            print(f'you can do everything')
        else:
            raise ValueError("unknown user type")
    return show_customer_receipt

@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    print('Some very dangerous operation')

show_customer_receipt(user_type='user')


is_admin(user_type='admin')
