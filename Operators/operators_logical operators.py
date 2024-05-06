# not, and, or

# print(not 10) # False
# print(not 0) # True
# print(not 'abc') # False
# print(not '') # True
# print(not True) # False
# print(not None) # True

# print(not not 10) # True
# print(not not 0) # False
# print(not not 'abc') # True
# print(not not '') # False
# print(not not True) # True
# print(not not None) # False

# and, or - short-circuit

# Example 1

# my_list = []

# other_list =['a', 'b']

# print(my_list or other_list)

# Example 2


# my_list = [1, 2]

# my_dict = {'a': 3}

# print(my_list and my_dict)

# Example 3

# my_list = []

# my_list and print("List is not empty")

# if my_list:
#     print("List is not empty")
# else:
#     print("List is empty")    

# task

# option 1

# dict_1 = {'one': 1, 'two': 2,}

# dict_2 = {'two': 2, 'one': 1,}

# dict_1 == dict_2 and print("the dictionaries are the same")

# option 2

dict_1 = {'one': 5, 'two': 2,}

dict_2 = {'two': 2, 'one': 1,}

if dict_1 == dict_2:
    print("ЕThe dictionaries are the same")
else:
    print("The dictionaries are not the same")    