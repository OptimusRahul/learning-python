from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_activity
def make_chai(flavour):
    print(f"Making {flavour} chai")

make_chai("Masala")