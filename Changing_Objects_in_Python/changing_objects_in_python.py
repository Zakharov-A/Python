# Addresses of immutable objects

# print(id(10))
# a = 10

# print(id(a))

# ----

first_num = 10
# second_num = first_num

# print(id(first_num))  # 140733238426328
# print(id(second_num)) # 140733238426328

# second_num += 5
# print(second_num) # 15
# print(first_num) # 10

# print(id(second_num)) # 140733238426488
# print(id(first_num))  # 140733238426328
# print(id(15))

# ----

# Changing list

# my_list = [1, 2, 3]
# print(id(my_list))
# # 2879823073664

# other_list = [1, 2, 3]
# print(id(other_list))
# # 2879823075584 (the addresses change with each launch)

# other_list.append(4)
# print(id(other_list))
# # 2879823075584 (the addresses change with each launch)

# print(id([1, 2, 3]))
# # 2879823393728 (the addresses change with each launch)

# ----

# Changing dictionaries

# info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
# }

# print(id(info))

# info_copy = info

# print(id(info_copy))

# info['reviews_qty'] = 5

# print(id(info))
# print(info_copy)
# print(id(info_copy))

# ----

# my_info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
# }

# print(id(my_info))

# other_info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
# }
# other_info['rating'] = 5.0

# print(id(other_info))
# print(other_info)
# print(my_info)

# ----

# How to avoid altering copies

# info = {
#     'name': 'Bogdan',
#     'is_instructor': True,
# }

# info_copy = info.copy()

# info_copy['reviews_qty'] = 5

# print(info_copy)
# print(id(info_copy))

# print(info)
# print(id(info))

# Nested mutable objects

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': [],
}

info_copy = info.copy()

info_copy['reviews'].append('Great course!')

print(info)
print(id(info))

print(info_copy)
print(id(info_copy))

info_copy['status'] = 'red!'

print(info)
print(info_copy)






