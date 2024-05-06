# operator **

# button = {
#     'width': 200,
#     'text': 'Buy',
# }

# red_button = {
#     **button,
#     'color': 'red'
# }

# print(red_button)
# # {'width': 200, 'text': 'Buy', 'color': 'red'}

# print(button)
# # {'width': 200, 'text': 'Buy'}

# ----

# merging dictionaries

# option 1

# button_info = {
#     'text': 'Buy'
# }

# button_style = {
#     'color': 'yellow',
#     'width': 200,
#     'height': 300,
# }

# button = {
#     **button_info,
#     **button_style
# }

# print(button)

# option 2

button_info = {
    'text': 'Buy',
    'width': 0,
    'height': 0,
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
    'price': 150,
}

button_other = {
    'price': 120,
    'color': 'green'
}

button = button_info | button_style | button_other

print(button)