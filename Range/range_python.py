# # range

# my_range = range(7)

# print(my_range)
# # range(0, 7)

# print(type(my_range))

# print(list(my_range))

# ----

# range specifying the start value,
#  end value and step

# my_range = range(10, 20, 3)

# print(type(my_range))

# print(my_range)

# print(list(my_range))

# print(my_range[0])
# print(my_range[1])
# print(my_range[2])
# print(my_range[3])

# ----

# range in cycles

# my_range = range(10, 20, 3)

# for n in my_range:
#     print(n)

# ----

# practice range

# my_range = range(5)

# print(my_range)
# print(type(my_range))

# for n in my_range:
#     print(n)

# print(my_range[0])

# ----

# for n in range(2, 7):
#     print(n)

# ----
    
# for n in range(12, 25, 5):
#     print(n)

# print(list(range(12, 25, 5)))    
# print(tuple(range(12, 25, 5)))    
# print(set(range(12, 25, 5)))    

# ----


# my_range = range(10, 30, 3)

# # print(dir(my_range))

# print(my_range.start)
# print(my_range.stop)
# print(my_range.step)
# print(my_range.index(13))
# print(my_range.count(11))
# print(my_range.count(10))
# print(list(my_range))

# # ----

my_range = range(2, 40, 4)
my_list = []

for num in my_range:
    my_list = num
    print(my_list)
