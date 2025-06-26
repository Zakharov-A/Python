import re


# def search_number() -> None:
#     my_string = "fsjf78 u95dfd3fl l1d 7"
#     nums =re.findall('[0-9]+', my_string)
#     print(nums)
#     numbers = []
#     for i in nums:
#         numbers.append(int(i))
#     print(numbers)    

# search_number()    


# def main() -> None:
#     my_string = "fsjf78 u95dfd3fl l1d 7"
#     numbers = []
#     temp = ''
#     for num in my_string:
#         if num.isdigit():
#             temp += num
#         elif temp:
#             numbers.append(int(temp))
#             temp = ''
#     if num.isdigit():
#         numbers.append(int(num))           
#     print(numbers)    


# main()

def searh_number_2() -> None:
    my_string = "fsjf78 u95dfd3fl l1d 7"
    numbers = [int(i) for i in re.findall(r'\d+', my_string)]
    print(numbers)

searh_number_2() 
