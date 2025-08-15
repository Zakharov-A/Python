
def decorator(name):
    print('decorator: ', name)

    def real_decorator(func):
        print('the decorator himself', func.__name__)

        def decorated(*args, **kwargs):
            print('before function', func.__name__)
            ret = func(*args, **kwargs)
            print('after function', func.__name__)
            return ret
        
        return decorated
    
    return real_decorator


@decorator('test')
def add(a, b):
    print('function add')
    return a + b


print('start')
r = add(10, 10)
print(r)
print('end')


