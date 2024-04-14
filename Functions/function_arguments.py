# positional arguments

# def sum_nums(a, b):
#     c = a + b
#     return c

# print(sum_nums(2, 5)) # ok

# print(sum_nums(2, 7, 9))
# # TypeError: sum_nums() takes 2 positional
# # arguments but 3 were given


# print(sum_nums(2))

# # TypeError: sum_nums() missing 1 required
# # positional argument: 'b'

# print(sum_nums())
# # TypeError: sum_nums() missing 2
# # required positional arguments: 'a' and 'b'

# ----

# combining arguments into a tuple # #

# def sum_nums(*args):
#     print(args)
#     print(type(args))
#     # print(args[0])
#     return sum(args)

# print(sum_nums(2, 3, 7))
# print(sum_nums())

# -----

# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# info = get_posts_info('Bogdan', 25)
# print(info)
# print(type(info))

# ----

# keyword arguments

# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# info = get_posts_info(name='Bogdan', posts_qty=25)
# print(info)
# print(type(info))

# ----

# combining arguments into a dictionary

# def get_posts_info(**person):
#     print(person)
#     # {'name': 'Bogdan', 'posts_qty': 25}

#     print(type(person)) # <class 'dict'>
#     info = (
#         f"{person['name']} wrote "
#         f"{person['posts_qty']} posts"
#     )
#     return info

# info = get_posts_info(name='Bogdan', posts_qty=25)
# print(info)

# ----

def get_posts_info(**person):
    print(person)
    print(type(person))
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info

info = get_posts_info(name='Bogdan', posts_qty=25, id=1351)
print(info)
print(type(info))

