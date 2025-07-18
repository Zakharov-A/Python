double = lambda x: x * 2

print(double(5))

def double(x: int) -> int:
    return x * 2


# my_list: list[int] = [1,5, 4, 6, 8, 11, 3, 12]
# new_list: list[int] = list(filter(lambda x: (x % 2 == 0), my_list ))
# print(new_list)

my_list: list[int] = [1, 5, 4, 6, 8, 11, 3, 12]
new_list: list[int] = list(map(lambda x: x * 2, my_list))
print(new_list)
print('Hello!')


