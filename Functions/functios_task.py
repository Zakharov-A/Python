
# def merge_list_to_dict(list_1, list_2):
#     list_1_copy = list_1.copy()
#     list_2_copy = list_2.copy()
#     list_merge = zip(list_1_copy, list_2_copy)
#     lists_dict = dict(list_merge)
#     return lists_dict

# fruit_list = ['Appel', 'Banana', 'Kiwi']
# price_fruit = [20, 50, 70]

# merge_dict = merge_list_to_dict(fruit_list, price_fruit)
# print(merge_dict)

# hobby_list = merge_list_to_dict(
#     ['footbal', 'karate', 'box'],
#     [2, 4, 5]
# )

# print(hobby_list)

# ----

def merge_list_to_dict(list_1, list_2):
    zipped_seg = zip(list_1, list_2)
    return dict(zipped_seg)

hobby_list = merge_list_to_dict(
    ['footbal', 'karate', 'box'],
    [2, 4, 5, 6]
)

print(hobby_list)
