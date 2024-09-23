a = 10

def my_fn():
    """Local scope"""
    a = True
    b = 15
    print(a)    # True
    print(b)    # 15


my_fn()

print(a)    # 10
# print(b)
# NameError: name 'b' is not defined
