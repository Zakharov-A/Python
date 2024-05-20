# my_number = -10

# if my_number > 0:
#     print(my_number, "is positive number")
# elif my_number < 0:
#     print(my_number, "is negative number")
# else:
#     print(my_number, "is zero") 

# ----

# using if in functions

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "One of the arguments is not an integer"
    
#     if a >= b:
#         return f"{a} more or equal {b}"
#     return f"{a} less {b}"

# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(4, 15))

# ----

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "One of the arguments is not an integer"
    elif a >= b:
        info = f"{a} more or equal {b}"
    else:
        info = f"{a} less {b}"
    return info    

print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))