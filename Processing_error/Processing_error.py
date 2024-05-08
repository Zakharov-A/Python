#ERROR/EXCEPT

# Example 1

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Error - Division by zero!")
# print('Continue...')        

# ----

# Example 2

# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(type(e))
#     print(e)

# print('Continue...')  

# Example 3

# try:
#     print('10' / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)    

# print('Continue...') 

# ----

# Example 4

# try:
#     print(10 / 2)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was no error")        

# print('Continue...') 

# ----

# Example 5

# try:
#     print(10 / 2)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was no error")        
# finally:
#     print('Continue...') 

# Exception 

# try:
#     print(10 / 0)
# except Exception as e:
#     print(e)       

# print('Continue...') 

# ----

# Creating errors using RAISE

def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b

try:
    divide_nums(10, 0)
except ValueError as e:
    print(e)

print('Continue...')