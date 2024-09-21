# my_motorbike = {
#     'brand': 'Ducati',
#     'price': 25000,
#     'engine_volume': 1.2,
# }
# print(my_motorbike)
# print(my_motorbike['price'])
# print(my_motorbike.get('model'))


# ----

# my_motorbike = {
#     'brand': 'Ducati',
#     'price': 25000,
#     'engine_volume': 1.2,
# }

# print(my_motorbike.get('model'))
# # None
# print(my_motorbike.get('brand'))
# # Ducati
# print(my_motorbike.get('price', 2))
# # 25000
# print(my_motorbike.get('qty', 4))
# 0
# my_dict = {}
# print(my_dict.__doc__)

# ----

# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

# my_disk['brand'] = 'Samsung'
# my_disk['brand'] = 'Xiomi'
# my_disk['price'] = 80

# print(my_disk)
# print(id(my_disk))

# print(my_disk.items())
# print(type(my_disk.items()))

# print(my_disk.keys())
# print(type(my_disk.keys()))
# print(list(my_disk.keys()))
# print(my_disk.popitem())
# print(my_disk.get('type', 'hdd'))
# print(my_disk)

# ----

my_disk = {}

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(len(my_disk))

new_disk = my_disk.copy()
new_disk['type'] = 'ssd'

print(my_disk)
print(new_disk)

# ----

# my_list = [('first', 0), ['second', True,]]


# my_str = [('first', 0), ['second', True]]

# my_dict = dict(my_str)
# print(my_dict)
# print(type(my_dict))

# my_dict = dict(my_list)
# print(my_dict)
# print(type(my_dict))
# print(my_dict['first'])
# print(my_dict.get('first'))

# my_dict['third'] = 500

# print(my_dict)

# del my_dict['first']

# print(my_dict)



