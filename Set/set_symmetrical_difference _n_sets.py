# # symmetric_difference

# my_set = {'abc', 'd', 'f', 'd'}

# copied_set = my_set.copy()

# my_set.add('t')
# copied_set.add('l')

# print(my_set.symmetric_difference(copied_set))

# 

a_set = {'abc', 'd', 'f', 'y'}
b_set = {'abc', 'd', 'f', 'l'}

print((a_set | b_set) - (a_set & b_set))
print(a_set.symmetric_difference(b_set))
