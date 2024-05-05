# Creation global variables

# a = 10

# def my_fn():
#     a = True
#     b = 15
#     print(a)
#     print(b)

# my_fn()

# print(a)

# ----

# a = 10

# def my_fn():
#     global a
#     a = 15


# print(a)
# my_fn()
# print(a) 

# ----

c = 5

def my_fn(a, b):
    d = 10
    print(c)
    print(a, b)
    print(dir())

my_fn('abc', 'xyz')
print(dir())
