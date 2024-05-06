# del instruction

my_dict = {'a': True, 'b': 10, 'c': 12}

del my_dict['a']

my_dict.__delitem__('b')

print(my_dict)