# Global scope and local scope
#  Example 1

# """Global scope"""
# a = 10

# def my_fn():
#     """Local scope"""
#     a = True
#     b = 15
#     print(a)    # True
#     print(b)    # 15  


# my_fn()

# print(a)    # 10
# print(b)
# NameError: name 'b' is not defined

# Example 2

"""Global scope"""
a = 5


def my_fn():
    """my_fn scope"""
    def inner_fn():
        """inner_fn scope"""
        print(a)    # 5
    inner_fn()


my_fn()