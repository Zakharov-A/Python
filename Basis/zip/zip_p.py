# Option 1

# def main() -> None:
#     cars = ["BMW", "AUDI", "Honda", "Mazda"]
#     men = ["Jonn", "Bob", "Mike", "Noah", "Jacob"]
#     cars_of_men = {}
#     for c, m in zip(cars, men):
#         print(c, m)
#         cars_of_men[c] = m
#     print(cars_of_men)    


# main()


# Option 2

def main() -> None:
    cars = ["BMW", "AUDI", "Honda", "Mazda"]
    men = ["Jonn", "Bob", "Mike", "Noah", "Jacob"]
    cars_of_men = dict(zip(cars, men))
    print(cars_of_men)
    

main()        


