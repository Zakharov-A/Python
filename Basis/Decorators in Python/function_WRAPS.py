from functools import wraps

def my_decorator(func):
    """Decorated"""
    @wraps(func)
    def decorated():
        """Function decorated"""
        func()
    return decorated


@my_decorator
def wrapped():
    """Wraparound function"""
    print("function wrapped")


print('start')
print(wrapped.__name__)
print(wrapped.__doc__)
