from pathlib import Path


def read_or_create_file() -> dict[str, str]:
    f = Path('parking.txt')
    cars: dict[str, str] = {}
    if f.exists():
        with open('parking.txt', 'r', encoding='utf-8') as file:
            for i in file.readlines():
                name, car = i[:-1].split(":")
                cars.update({name: car})
    else:
        file = open('parking.txt', 'w')
        file.close()
    return cars                


def write_file(cars: dict[str, str]) -> None:
    with open('parking.txt', 'w', encoding='utf-8') as file:
        for name, car in cars.items():
            file.writelines(f'{name}:{car}\n')


def parking() -> None:
    cars = read_or_create_file()

    
    while True:
        command = input(
            "\n1 - Add\n" \
            "2 - Delete\n" \
            "3 - View\n" \
            "4 - Modify\n" \
            "5 - Write to file\n" \
            "6 - Exit from the programm\n"\
            "Enter the command: "
        )
        if command == '1':
            owner = input("Enter the owner's name: ")
            if cars.get(owner):
                print("The owner's car with that name is already in the parking lot.")
                continue
            car = input("Enter the make of the car: ")
            cars[owner] = car

        elif command == '2':   
             owner = input("Enter the owner's name: ")
             if cars.get(owner):
                 cars.pop(owner)
                 print(f"{owner} drove away from the parking lot.")
             else:
                 print(f"{owner} name wasn't found.")

        elif command == '3':
            print("\nLocated now in the parking lot:")
            for owner, car in cars.items():
                print(f"{owner} - {car}")

        elif command == '4':
            owner = input("Enter the owner's name: ")
            if cars.get(owner):
                car = input("Enter the mark of the car: ")
                cars[owner] = car
            else:
                print(f"Name {owner} not found")

        elif command == '5':
            write_file(cars)
            print("Data recorded.")                        

        elif command == '6':
            print("Termination of the program.") 
            break       

parking()                             