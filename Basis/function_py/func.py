
# def main():
#     for i in "Hello Django School":
#         print(i)

# if __name__ == "__main__":
#     main()

# def main():
#     name = "Jora".upper()
#     n = 0
#     for i in name:
#         n += 1
#         print(n, i)

# if __name__ == "__main__":
#     main()

# def calc(a, b):
#     c = a + b
#     return c

# result = calc(1, 3)
# print(result)

# def main():
#     name = "Jora".upper()
#     for n, i in enumerate(name):
#         print(n, i)

# if __name__ == "__main__":
#     main()

# ----

# def calc(a, b=5):
#     c = a + b
#     return c

# result = calc(1, 2)
# print(result)

# result2 = calc(4)
# print(result2)

# ----

# def my_func(*args):
#     print(args)
#     print(type(args))

# my_func(1, 2, 'Hi', 5,5)
# my_func(1, 2, 3, [1, 2, 'Hi'], {1: 'good'}) 

# ----

# def my_func2(*args):
#     print(args)

# my_list = (1, 2, 3, 'Hi', 4.5)
# my_func2(*my_list)

# ----

# def my_func3(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# my_func3(key=1, word='Hi', number=4)  

# ----

# def my_func3(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# my_test_dict = {'key': 1, 'word': 'Hi', 'number': 4}
# my_func3(**my_test_dict)   
 
# ----

# def my_func4(*args, **kwargs):
#     print(args)
#     print(type(args))
#     print(kwargs)
#     print(type(kwargs))

# my_test_dict = {'key': 1, 'word': 'Hi', 'number': 4}
# my_func4(*my_test_dict)
# print()
# my_func4(**my_test_dict)
# print()
# my_func4(my_test_dict)  

# ----

#  def my_func(a, b=2, *args, **kwargs): ...

# ----

def my_func5(a, b=2, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


my_func5('test', 1, 2, 3, key=1, key2=44)

print()

def my_func6(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


my_func6('test', 1, 2, 3, key=1, key2=44)
