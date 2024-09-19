# Creating a tuple and outputting the value by index

# posts_ids = (151, 245, 762, 167)

# print(posts_ids[0])
# print(posts_ids[1])
# print(posts_ids[-1])

# ----

# my_nums = (10, 5, 100, 0)
# print(type(my_nums))

# ----

# Lists and dictionaries inside a tuple

# users = (
#     {
#         'user_id': 134,
#         'user_name': 'Anton',
#         'user_city': 'Berlin',
#     },
#     {
#         'user_id': 831,
#         'user_name': 'Bob',
#     }
# )

# print(users[1]['user_id'], users[0]['user_city'],
#       users[1]['user_name'])
# print(users)
# users[1]['user_name'] = 'Riddick'
# print(users)
# del users[0]['user_id']
# print(users)

# ----

# using variables in tuples

# my_fruit = 'apple'
# other_fruit = 'banana'
# new_fruit = 'lime'

# all_fruits = (my_fruit, other_fruit, new_fruit)

# print(all_fruits) # ('apple', 'banana', 'lime')
# print(all_fruits[1])

# ----

# union of tuples

# internal_ids = (151, 245)
# external_ids = (624, 451, 941)

# all_ids = internal_ids + external_ids

# print(all_ids)
# # (151, 245, 624, 451, 941)

# ----

# internal_ids = (151, 245)
# external_ids = (624, 451, 941)

# all_ids = internal_ids.__add__(external_ids)

# print(all_ids)

# ----

# tuple methods
# count

# posts_ids = (151, 245)

# posts_ids_list = list(posts_ids)
# posts_ids_list.append(351)

# print(posts_ids_list)
# print(posts_ids)
# print(posts_ids.count(245))

# posts_ids_tuple = tuple(posts_ids_list)

# print(posts_ids_tuple)

# ----

# index

# converting a tuple to a list

# my_nums = (10, 5, 100, 0, 5, 5)
# print(my_nums.index(5, 2))

# my_list = list(my_nums)

# my_list.append(7)

# print(my_list)
# print(my_nums)

# ----

# my_nums = tuple(my_list)

# print(my_nums)

# creating a tuple from a string

# my_touple = tuple('abcd')

# print(my_touple) # ('a', 'b', 'c', 'd')

# ----

# my_touple_dictionaries = tuple(
#     {
#         'first': 1,
#         'second': 3,
#         'third': 4,
#     }
# )

# print(my_touple_dictionaries)

# ----

# tuple_one = (11, True, 'Hallo')
# tuple_two = ('red', 'zed', 'bob')

# print(tuple_one + tuple_two)

# tuple_full = tuple_one.__add__(tuple_two)

# print(tuple_full)
# print(type(tuple_full))

# Practice of corteges

# my_nums = (10, 5, 100, 0, 5, 5)

# index_one = my_nums.index(5)
# index_two = my_nums.index(5, index_one + 1)

# print(index_two)

# ----

# my_nums = (10, 5, 100, 0, 5, 5)

# my_list = list(my_nums)

# my_list.append(7)

# print(my_nums)

# my_nums = tuple(my_list)

# print(my_nums)

# ----

my_tuple_1 = (12, 14)

my_tuple_2 = (16, 18)

my_tuple_3 = my_tuple_1 + my_tuple_2

print(my_tuple_3)

