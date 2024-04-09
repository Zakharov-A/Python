# Addresses of immutable objects

# print(id(10))
# a = 10

# print(id(a))

# ----

# Changing list

# my_list = [1, 2, 3]
# print(id(my_list))

# other_list = [1, 2, 3]
# print(id(other_list))

# other_list.append(4)
# print(id(other_list))

# print(id([1, 2, 3]))

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






