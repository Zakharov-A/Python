

# my_fruits = ['apple', 'banana', 'lime']

# my_apple, my_banana, my_lime = my_fruits

# print(my_apple)
# print(my_banana)
# print(my_lime)

# ----

# Use * when unpacking

# my_fruits = ['apple', 'banana', 'lime']

# my_apple, *remaining_fruits = my_fruits

# print(my_apple)
# print(remaining_fruits)

# print(type(remaining_fruits))

# ----

# Unpacking a list into positional arguments

# user_data = ['Jimmy', 30]

# def user_info(name, comments_qty):
#     if not comments_qty:
#         return f"{name} has no comments" 
    
#     return f"{name} has {comments_qty} comments"

# print(user_info(*user_data))

# ----

user_data = ['Jimmy', 30]

def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments" 
    
    return f"{name} has {comments_qty} comments"

my_name, my_comments_qty = user_data

print(user_info(my_name, my_comments_qty))
