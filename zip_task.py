# Create a list of prices
# and a list of products, convert
# into a combined
# list and into a dictionary

fruts_list = ['Banana', 'Appel', 'Orange', 'Kiwi']

price_list = [80, 40, 50, 95]

full_zip = zip(fruts_list, price_list)

fruts_price_list = list(full_zip)

print(fruts_price_list)
# [('Banana', 80), ('Appel', 40), ('Orange', 50), ('Kiwi', 95)]

fruts_price_dict = dict(fruts_price_list)

print(fruts_price_dict)
# {'Banana': 80, 'Appel': 40, 'Orange': 50, 'Kiwi': 95}
