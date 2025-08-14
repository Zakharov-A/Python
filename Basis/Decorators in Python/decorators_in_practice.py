
# def memorize(func):
#     memo = {}
#     print("memorize")

#     def wrapper(*args):
#         print("before function")
#         rv = func(*args)
#         print("after function")
#         return rv
    
#     return wrapper

# @memorize
# def func(a, b) -> int:
#     print('func')
#     return a * b


# print('start')
# print(func(2, 5))
# print('end')
# print(func(2, 5))

###


# def memorize(func):
#     memo = {}

#     def wrapper(*args):
#         if args in memo:
#             print('memo')
#             return memo[args]
#         else:
#             print('rv')
#             rv = func(*args)
#             memo[args] = rv
#             return rv
    
#     return wrapper

# @memorize
# def func(a, b) -> int:
#     return a * b


# print('start')
# print(func(2, 5))
# print(func(2, 5))
# print('end')


###


def error_handler(fun):
    def wrapper(*args):
        rv = 0
        try:
            rv = fun(*args)
        except:
            print(f"Error in function - {fun.__name__}")
        return rv

    return wrapper


@error_handler
def dev(a, b) -> int:
    return a / b


print(dev(10, 2))
print(dev(10, 0))