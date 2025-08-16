
# class MyClassFunc:
#     def __call__(self, a, b):
#         print(a + b)


# fun = MyClassFunc()
# fun(2, 6)


# class MyDecorator:
#     def __init__(self, func):
#         print('method __init__')
#         self.func = func


#     def __call__(self, *args, **kwargs):
#         print('before call wrapped', self.func.__name__)
#         rv = self.func(*args, **kwargs)
#         print('after call wrapped')
#         return rv 


# @MyDecorator
# def func(a, b, c) -> None:
#     return (a + b) * c



# print(func(2, 5, 2))
# print(func(3, 10, 4))


###

class MyDecorator2:
    def __init__(self, name):
        print('__init__:', name)
        self.name = name


    def __call__(self, func):
        def wrapper(a, b):
            print('before function')
            func(a, b)
            print('after function')
        return wrapper

@MyDecorator2("test2")
def add(a, b):
    print('function add:', a, b)


print('start')
add(2, 5)   
print('end')

