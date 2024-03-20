# range

# my_range = range(7)

# print(my_range)
# # range(0, 7)

# print(type(my_range))
# # <class 'range'>

# print(list(my_range))
# # [0, 1, 2, 3, 4, 5, 6]

# range specifying the start value,
#  end value and step

# my_range = range(10, 20, 3)

# print(type(my_range))
# # <class 'range'>

# print(my_range)
# # range(10, 20, 3)

# print(list(my_range))
# # [10, 13, 16, 19]

# print(my_range[0])
# print(my_range[1])
# print(my_range[2])
# print(my_range[3])
# print(my_range[4]) # IndexError: range object index out of range

# range in cycles

# my_range = range(10, 20, 3)

# for n in my_range:
#     print(n)

# practice range

# my_range = range(5)

# print(my_range)
# print(type(my_range))
# print(my_range[0])

# for n in my_range:
#     print(n)

# for n in range(12, 25, 5):
#     print(n)

# print(list(range(12, 25, 5)))    
# print(tuple(range(12, 25, 5)))    
# print(set(range(12, 25, 5)))    

# my_range = range(10, 30, 5)

# # print(dir(my_range))

# # print(my_range.start)
# # print(my_range.stop)
# # print(my_range.step)
# print(my_range.index(20))
# print(my_range.count(11))

my_new_range = range(5, 30, 5)

my_list = []


for n in my_new_range:
    my_list = n
    print(n)