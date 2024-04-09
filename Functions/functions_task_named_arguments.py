# Task 1

# def merge_list_to_do(list_names, list_prices):
#     list_names_copy = list_names.copy()
#     list_prices_copy = list_prices.copy()
#     list_merge = zip(list_names_copy, list_prices_copy)
#     lists_dict = dict(list_merge)
#     return lists_dict

# fruit_list = ['Appel', 'Banana', 'Kiwi']
# price_fruit = [20, 50, 70]

# merge_dict = merge_list_to_do(list_names = fruit_list, list_prices = price_fruit)
# print(merge_dict)

# hobby_list = merge_list_to_do(
#     ['footbal', 'karate', 'box'],
#     list_prices = [2, 4, 5],
# )

# print(hobby_list)


# def merge_list_to_do(name_list, price_list):
   
#     full_list = list(zip(name_list, price_list))
#     return full_list
     

# fruit_list = ['Appel', 'Banana', 'Kiwi']
# price_fruit = [20, 50, 70]

# list_merge = merge_list_to_do(name_list=fruit_list, price_list=price_fruit)
# print(list_merge)

# list_hobbys = ['footbal', 'karate', 'box']
# prices_hobbys = [2, 4, 5]

# hobby_list = merge_list_to_do(list_hobbys, price_list=prices_hobbys)
# print(hobby_list)

# Task 2

def update_car_info(**cars_inf):
    cars_inf_copy = cars_inf.copy()
    cars_inf_copy['is_available'] = True
    return cars_inf_copy

car_name = 'Lada'
car_price = 60

car_info = update_car_info(brand=car_name, price=car_price, id='test' )
print(car_info)


    