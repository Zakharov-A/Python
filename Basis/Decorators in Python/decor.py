from __future__ import annotations
from typing import Callable

# def first(msg) -> None:
#     print(msg)


# first("Hello")

# second = first
# second("Hello")


###


# def is_called() -> Callable[[], None]:
#     def is_returned() -> None:
#         print("Hi Bro!")
#     return is_returned


# new: Callable[[], None] = is_called()

# new()

###


# def make_pretty(func: Callable[[], None]) -> Callable[[], None]:
#     def inner() -> None:
#         print("I got decorated")
#         func()
#     return inner


# def ordinary():
#     print("I am ordinary")


# ordinary()
# pretty = make_pretty(ordinary)
# pretty()


# @make_pretty
# def ordinary() -> None:
#     print("I am ordinary")

# ordinary() 


###

# def smart_divide(
#         func: Callable[[float, float], float]
#         ) -> Callable[[float, float], float | None]:
#     def inner(a: float, b: float) -> float | None:
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
        
#         return func(a, b)
#     return inner


# @smart_divide
# def divide(a: float, b: float) -> None:
#     print(a/b)


# divide(2, 5)
# divide(10, 0) 
# divide(0, 5)   

###    


def smart_divide(func):
    def inner(*args, **kwargs):
        print("I am going to divide")
        return func(*args, **kwargs)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

# divide(2, 5)

###

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner
    

@star
@percent
def printer(msg):
    print(msg)

printer("Hi my friend!")    