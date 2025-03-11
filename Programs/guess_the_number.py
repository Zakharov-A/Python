import random


def main() -> None:
    times: int = 0
    while True:
        random_number: int = random.randint(0, 3)
        user_number: int = int(input("Enter the number from 0 to 3: "))

        if user_number == random_number:
            print("You won!")
        else:
            print("You lost!")

        times += 1

        if times == 3:
            print("Game over")
            break     

        answer = input("Do you want to continue? y/n: ")
        if answer == 'y':
            continue
        else:
            print("Goodbye!")
            break

         


if __name__=="__main__":
    main()    