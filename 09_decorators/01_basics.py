from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function is called.")
        func()
        print("After function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print(say_hello.__name__)