# my_fruits = {'apple', 'banana', 44, 44, 'banana'}
# print(my_fruits)
# print(type(my_fruits))
# print(len(my_fruits))

# my_set = {[10, 10], 5, 15, 15}
# # TypeError: unhashable type: 'list'

# my_set = {(10, 10), 5, 15, 15}
# my_set_2 = set()

# print(my_set_2)
# print(type(my_set_2))

# print(my_set)
# print(len(my_set))

# del my_set[0]
# # TypeError: 'set' object doesn't
# #  support item deletion

# set methods

# add

# photo_sizes = {'1920x1080', '800x600'}

# photo_sizes.add('1024x768')

# print(photo_sizes)
# # {'1024x768', '1920x1080', '800x600'}

# # union, intersection

# photo_sizes = {'1920x1080', '800x600'}
# other_sizes = {'800x600', '1024x768', '300x300'}

# # all_sizes = photo_sizes.union(other_sizes)
# all_sizes = photo_sizes | other_sizes

# print(all_sizes)

# common_s = photo_sizes & other_sizes
# # common_s = photo_sizes.intersection(other_sizes)

# print(common_s)

# issubset

# nums = {10, 5, 35}
# other_nums = {20, 5, 12, 10, 35}

# res = nums.issubset(other_nums)
# res_2 = other_nums.issuperset(nums)

# print(res_2)
# print(res)

my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}

# print(my_set.intersection(other_set))
# print(my_set.intersection(['a', 'b', 'c', 'd']))
# print(other_set.intersection(my_set))
# print(my_set.union(other_set))
# print(other_set.issubset(my_set))
# print(my_set.issuperset(other_set))
# print(my_set.difference(other_set))
# print(my_set - other_set)
# print(my_set & other_set)
# print(my_set | other_set)
# my_set.discard('d')
# my_set.discard('def')
# my_set.remove('def') # KeyError: 'def'
# my_set.remove('y')

copied_set = my_set.copy()

my_set.add('r')
copied_set.add('k')
print(copied_set)

print(my_set)

print(my_set & copied_set)
print(my_set.symmetric_difference(copied_set))
print(my_set.intersection(copied_set))