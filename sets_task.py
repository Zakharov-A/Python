int_set = {2, 4, 5, 88}
int_set.add(45)
print(int_set)

my_set_2 = {1, 'Hi', 3, 88, 4}

my_set_difference = int_set.intersection(my_set_2)
print(my_set_difference)
my_list_difference = list(my_set_difference)
print(my_list_difference)
print(type(my_list_difference))