# def func_one() -> None:
#     animals: set[str] = {"Tiger", "Cat", "Dog", "Pig"}
#     print(animals)
#     print(type(animals))

# func_one()  


# def func_two() -> None:
#     animals = {"Tiger", "Cat", "Tiger", "Dog", "Pig", "Dog"}
#     print(animals)

# func_two()    


# def func_three() -> None:
#     animals: set[str] = {"Tiger", "Cat"}
#     print(animals)
#     animals.add("Dog")
#     print(animals)

# func_three() 

# def func_four() -> None:
#     animals: set[str] = set('Tiger')
#     print(animals)
#     animals.add("Dog")
#     print(animals)

# func_four()

# def func_five() -> None:
#     animals: set[str] = {"Tiger", "Cat"}
#     print(animals)
#     # animals.update("Dog")
#     # print(animals)
#     dog = {"Dog", "Cat"}
#     result1 = animals.intersection(dog)
#     result2 = animals.difference(dog)
#     print(result1)
#     print(result2)

# func_five()

# def func_six() -> None:
#     animals = {"Tiger", "Cat"}
#     for i in animals:
#         print(i)

# func_six()


# def func_seven() -> None:
#     animals = {"Tiger", "Cat"}
#     print(animals)
#     print(type(animals))

# func_seven()    

def two_list() -> None:
    list_names: list[str] = ['John', 'Bob', 'Mike', 'Anna']
    get_names: list[str] = ['Bob', 'Elena', 'Anna', 'Victor']
    new_list1: list[str] = list(set(list_names + get_names))
    new_list2: list[str] = list(set(list_names) - set(get_names))
    new_list3: list[str] = list(set(list_names) ^ set(get_names))
    new_list4: list[str] = list(set(list_names) & set(get_names))

    all_list: tuple[list[str]] = new_list1, new_list2, new_list3, new_list4

    for lst in all_list:
        print(lst)

two_list()        
