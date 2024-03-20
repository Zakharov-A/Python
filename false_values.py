# False values
# int 0
# float 0.0
# complex 0j
# dict {}
# list []
# tuple ()
# set set()
# range range(0)
# str ""

# Example 1

# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(None))
# print(not not {})
# print(not not {'a': 10})

# Example 2


def check_my_list(my_list):
    if my_list:
        print("List has elements")
    else:
        print("List has not element") 


my_list_1 = [1, 2, 3]
my_list_2 = []
my_list_3 = [' ']

check_my_list(my_list_1)           
check_my_list(my_list_2)           
check_my_list(my_list_3)           