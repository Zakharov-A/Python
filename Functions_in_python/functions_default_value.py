from datetime import date


# # Functions default value

# def mult_by_factor(value, multiplier=2):
#     return value * multiplier

# print(mult_by_factor(10, 2)) # 20
# print(mult_by_factor(5)) # 5
# print(mult_by_factor(value=3, multiplier=4))
# # 12

# ----

# variant 1 

# def get_weekday():
#     return date.today().strftime('%A')


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy


# initial_post = {
#     'id': 243,
#     'author': 'Bogdan',
# }

# post_with_weekday = create_new_post(initial_post)

# print(post_with_weekday)
# {'id': 243, 'author': 'Bogdan', 'created_on_weekday': 'Friday'}

# print(initial_post)
# # {'id': 243, 'author': 'Bogdan'}

# ----

# variant 2

def get_weekday():
    return date.today().strftime('%A %d.%m.%Y')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

post_with_weekday = create_new_post(post=initial_post)

print(post_with_weekday)
# {'id': 243, 'author': 'Bogdan', 'created_on_weekday': 'Monday'}

# print(initial_post)
# # {'id': 243, 'author': 'Bogdan'}
