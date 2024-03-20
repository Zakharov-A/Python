# Creating Functions

# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c


# res = my_fn(10, 3)
# print(res)


# def my_fn(a, b, c):
#     a = a + 1
#     b = b + 1
#     c = a + 1
#     d = a + b + c
#     return d

# res = my_fn(3, 6, 4)
# print(res)
# 16

# Shortest function

# def my_fn():
#     pass

# print(my_fn()) # None

# Passing immutable objects

# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c

# num_one = 10
# num_two = 5

# res = my_fn(num_one, num_two)
# print(res) # 16
# print(num_one) # 10

# Passing mutable objects inside a function

# def increase_person_age(person):
#     print(id(person))
#     person['age'] += 1
#     return person

# person_one = {
#     'name': 'Bob',
#     'age': 21,
# }

# print(id(person_one))

# increase_person_age(person_one)
# print(person_one['age']) # 22

# How to avoid
#  changing external objects
#  in a function

# def increase_person_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy

# person_one = {
#     'name': 'Bob',
#     'age': 21
# }

# new_person = increase_person_age(person_one)
# print(new_person['age']) # 22
# print(person_one['age']) # 21

# print(), input()

# print("Hello Python")
# print(print) # <built-in function print>

name = "kyky"

print(name.capitalize())
print(name.casefold())

# dir()

# print(dir('Hello'))

# Methods

# name = 'Bogdan'
# print(name.upper())
# print( dir(__builtins__))


