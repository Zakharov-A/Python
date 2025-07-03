def main() -> None:
    students: dict[str, str] = {}
    while True:
        command = input(
            "1 - Add\n" \
            "2 - Show raings\n" \
            "3 - Exit from programm\n" \
            "Enter command\n"
            )
        if command == '1':
            name: str = input("Enter name: ")
            while True:
                try:
                    grade: int = int(input("Enter grade: "))
                except ValueError:
                    print("You enter not a number! Enter number please!")
                    continue
                else:    
                    students[name] = grade

main()            

        