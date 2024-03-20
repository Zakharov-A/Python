# statements: =, if ..., import ...,  

import datetime     # Импортирование модуля

print(datetime.MINYEAR)
print(datetime.MAXYEAR)

my_name = 'Bogdan'  # Присваевание значения


if my_name:         # Условная инструкция
    print(my_name)


def my_func(a, b):
    c = a + b
    return c


print(my_func(10, 2))