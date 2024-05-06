# greeting = "Hello from Python"
# greeting_letters = list(greeting)

# print(greeting_letters)
# ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm',
#  ' ', 'P', 'y', 't', 'h', 'o', 'n']

# my_dict = {'a': 10, 'b': True}
# my_dict_keys = list(my_dict)

# print(my_dict_keys)
# ['a', 'b']

# arithmetic operations in lists

# ratings = [2.5, 5.0, 4.3, 3.7]

# print(min(ratings)) # 2.5
# print(max(ratings)) # 5.0
# print(sum(ratings)) # 15.5

# print(sum(ratings)/len(ratings)) # 3.875

# merging lists

# my_ratings = [2.5, 5.0]
# other_ratings = [3.7, 4.5, 4.9]

# all_ratings = my_ratings + other_ratings
# print(all_ratings)
# [2.5, 5.0, 3.7, 4.5, 4.9]

# list slicing

# ratings = [2.5, 5.0, 4.3, 3.7, 4.5]

# first_two_ratings = ratings[:2]
# print(first_two_ratings) # [2.5, 5.0]

# middle_ratings = ratings[1:-1]
# print(middle_ratings) # [5.0, 4.3, 3.7]

# last_two_ratings = ratings[-3:]
# print(last_two_ratings) # [3.7, 4.5]

# print(ratings)

# copying lists variant 0

# my_cars = ['BMV', 'Mercedes']

# copied_cars = my_cars

# copied_cars.append('Audi') 

# print(copied_cars)

# ['BMV', 'Mercedes', 'Audi']

# print(my_cars) # ['BMV', 'Mercedes']

# print(id(my_cars) == id(copied_cars)) # True


# copying lists variant 1

# my_cars = ['BMV', 'Mercedes']

# copied_cars = my_cars[:]

# copied_cars.append('Audi') 

# print(copied_cars)

# print(my_cars) # ['BMV', 'Mercedes']

# print(id(my_cars) == id(copied_cars)) # False

# ---- copying lists variant 2

# my_cars = ['BMV', 'Mercedes']

# copied_cars = my_cars.copy()

# copied_cars.append('Audi') 

# print(copied_cars)
# # ['BMV', 'Mercedes', 'Audi']

# print(my_cars) # ['BMV', 'Mercedes']

# print(id(my_cars) == id(copied_cars)) # False

# ---- copying lists variant 3

# my_cars = ['BMW', 'Mercedes']

# copied_cars = list(my_cars)

# copied_cars.append('Audi')

# print(copied_cars)

# print(my_cars)

# print(id(my_cars) == id(copied_cars))



# count the number
#  of instances of a specified object

# my_nums = [10, 50, 0, 5, 5, 100]

# res = my_nums.count(5)

# print(res)

# # adding an element to a list

# my_nums = [10, 50, 0, 5, 5, 100]

# my_nums.append(25)

# print(my_nums)

# Extend list by appending
#  elements from the iterable.

# my_nums = [10, 50, 0, 5, 5, 100]

# my_nums.extend('abc')

# print(my_nums)

# Return a shallow copy of the list.

# my_nums = [10, 50, 0, 5, 5, 100]

# other_nams = my_nums.copy() # my_nums[:]

# my_nums.append(3)
# other_nams.clear()

# print(id(other_nams))
# print(id(my_nums))

# print(my_nums, other_nams)

# ---- Tasks 1

my_list = [1, True, 5.6, 'Hi', [1, 2, 3]]

print(my_list)

print(len(my_list))

my_list.pop(2)

print(my_list)

print(len(my_list))

reversed_list = list(reversed(my_list))
print(reversed_list)


my_new_list = [23, 4.5]

my_list = my_list + my_new_list
print(my_list)
print(len(my_list))

# ----
# ----
 
# Task 2

my_list_1 = [1, 2, 3]
my_list_2 = ['hi', 'hallo', 'Guten Tag']

my_list_sum = my_list_1 + my_list_2

print(my_list_sum)

print(my_list_1.__add__(my_list_2))

print(my_list_1)
print(my_list_2)


