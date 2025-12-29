from functools import wraps

def authorized(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print(f"Access denied for {user_role}")
            return None
        else:
            return func(user_role)
    return wrapper

@authorized
def make_chai(user, flavour='masala'):
    print(f"{user} is making {flavour} chai")

make_chai("admin")
make_chai("user")