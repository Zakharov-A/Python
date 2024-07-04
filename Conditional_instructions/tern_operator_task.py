# my_img = ('1920', '1080')

# info = f"{my_img[0]}x{my_img[1]}" if len(
#     my_img) == 2 else "Incorrect image formatting"

# ----

# my_img = ('2080', '1600')

# print(f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Incorrect image formatting")

# print(info)

# Task 1

my_img = ('2080', '1600')

if len(my_img) == 2:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info = "Incorrect image formatting"    

print(info)

 # Task 2

my_str = "Very, very, very long string!"

print("String is long" if len(my_str) > 40 else "String is short")
   
        