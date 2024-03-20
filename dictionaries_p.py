# my_motorbike = {
#     'brand': 'Ducati Verona',
#     # 'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
# }

# print(my_motorbike)

# other_motorbike = {
#     # 'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
#     'brand': 'Ducati Verona',

# }

# print(other_motorbike)

# print(my_motorbike == other_motorbike)
# # True
# print(id(my_motorbike) == id(other_motorbike))


# changing 
# and deleting values in a dictionary

# changing 

# my_motorbike = {
#     'brand': 'Ducati Verona',
#     # 'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
# }


# print(my_motorbike['full price'])
# print(dir(my_motorbike))

# print(my_motorbike['full price'])




# print(my_motorbike)
# print(my_motorbike)

# print(my_motorbike['brand'])
# time 5:00:05
# using variables in dictionaries 

# my_motorbike['full price'] = 50000


# my_motorbike['is_new'] = True

# print(my_motorbike)

# del my_motorbike['engine_vol']



# my_motorbike = {
#     'brand': 'Ducati Verona',
#     # 'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
# }

# print(my_motorbike)

# key_name = 'City'

# my_motorbike[key_name] = 'Berlin'
# my_motorbike['brand'] = 'BMW'

# print(my_motorbike)


# my_motorbike = {
#     'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
#     'price_info': {
#         'price': 40000,
#         'is_available': True,
#     }
# }

# print(my_motorbike['price_info']['price'])
# # 25000
# print(my_motorbike['price_info']['is_available'])
# # True


# my_motorbike = {
#     'brand': 'Ducati Verona',
#     'full price': 25000,
#     'engine_vol': 1.2,
#     'price_info': {
#         'price': 40000,
#         'is_available': {
#             'one': 15000,
#             'two': 14000,
#         },
#     },
# }

# print(my_motorbike['price_info']['price'])
# # 25000
# print(my_motorbike['price_info']['is_available'])
# # True
# print(my_motorbike['price_info']['is_available']['one'])

# brand = 'Ducati'
# bike_price = 25000
# engine_volume = 1.2

# my_motorbike = {
    # 'brand': brand,
    # 'price': bike_price,
    # 'engine_volume': engine_volume,
# }

# print(my_motorbike)
# {'brand': 'Ducati', 'price': 25000, 1.2: 1.2}

# print(len(my_motorbike))
# 3

# del my_motorbike['price']

# print(my_motorbike)

# print(len(my_motorbike))
# 2


brand = 'Ducati'
bike_prace = 25000
engine_volume = 1.2

my_motorbike = {
    'brand': brand,
    'price': bike_prace,
    'engine_vol': engine_volume
}

print(my_motorbike)
# {'brand': 'Ducati', 'price': 25000, 'engine_vol': 1.2}

# Dictionary length
print(len(my_motorbike))
# 3

del my_motorbike['engine_vol']

print(len(my_motorbike))

