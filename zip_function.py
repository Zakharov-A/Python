# # zip 

fruits = ['apple', 'banana', 'lime', 'Apple']

quantities = [100, 70, 50, 20]

availability = [True, False, False, True]

fruit_qtys_zip = zip(fruits, quantities, availability)

print(fruit_qtys_zip)

print(type(fruit_qtys_zip))

fruit_qtys_zip = list(fruit_qtys_zip)

print(fruit_qtys_zip)

print(type(fruit_qtys_zip))

# ----

# convert zip to dictionary

fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)
print(type(fruit_qtys_zip))

fruit_qtys_dict = dict(fruit_qtys_zip)

print(fruit_qtys_dict)
