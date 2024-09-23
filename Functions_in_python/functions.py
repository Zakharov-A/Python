#-- Example 1 --
# name = input("Enter your name: ")
# password = input(f"{name} enter your password: ")

# print(f"Your name is: {name}")
# print(f"Your password is: {password}")

#-- Example 2 --
# name ='Red'
# print(dir(name))

#-- Example 3 --
# name = 'Red'
# print(name.upper())

#-- Example 4 --
# print(dir(__builtins__))

 
# def print_name_function(name):
#     print(name)


# print_name_function('Denis')    # Denis


# def hello(name):
#     print("Hello there!", name)


# hello('Bogdan')
# hello('Alice')

#-- Example 5 -- 

# def sum_nums(a, b):
#     sum = a + b
#     print(sum)


# sum_nums(10, 5)
# sum_nums(50.5, 20)


#-- return --


def sum_nums(a, b):
    sum = a + b
    return sum


first_num = sum_nums(10, 5)
print(first_num)
second_num = sum_nums(50.5, 20)
print(second_num)

print(sum_nums(sum_nums(50.5, 20), 30))

# third_num = sum_nums(sum_nums(50.5, 20), 30)
# print(third_num)


# def sum_none_nums(a, b):
#     sum = a + b

# print(sum_none_nums(4, 4))
