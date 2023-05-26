import time

def speed_calc_decorator(func):
    def wrapper_function():
        start_time = time.time()
        func()
        end_time = time.time()
        speed = end_time - start_time
        print(f'{func.__name__} run speed: {speed}')

    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authentication_decorator(func):
    def wrapper_func(*args, **kwargs):
        if args[0].is_logged_in:
            func(args[0])
    return wrapper_func

@is_authentication_decorator
def create_blog_post(user:User):
    print(f"This is {user.name}'s new blog post")

new_user = User('Illia')
create_blog_post(new_user)


# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper_func(*args):
        result = ''

        calculate = func(*args)

        result += f'You called {func.__name__}{args}\n'
        result += f'It returned: {calculate}'

        return result

    return wrapper_func


# Use the decorator 👇
@logging_decorator
def add_nums(*args):
    return sum(args)


print(add_nums(1, 2, 3))