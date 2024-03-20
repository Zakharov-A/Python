# immutable objects: str, int, bool, tuple, None, Range


# mutable objects: list, dictionary, set, user-defined classes

# Example 1

# print(id(10))
# my_num = 10

# print(id(my_num))

# my_num = 9

# print(id(my_num))

# print(id(9))

# my_num_2 = 9

# print(id(my_num_2))

# Example 2

my_name = 'Andre'

print(id(my_name)) # Данные меняются при запуске

print(id(9)) # 140714064689848 (Остаются не изменными)

my_num = 9

print(id(my_num)) # 140714064689848 (Остаются не изменными)

other_num = my_num

print(id(other_num)) # 140714064689848 (Остаются не изменными)

