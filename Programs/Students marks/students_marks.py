def add_students() -> tuple[str, int]:
    name: str = input("Enter name: ")
    while True:
        try:
            grade: int = int(input("Enter grade: "))
        except ValueError:
            print("You enter not a number! Enter number please!")
            continue
        else:    
            return name, grade    


def sort_students(students: dict[str, int]) -> None:
    good_grade = "Got into university: "
    bad_grade = "Didn't get into university: "
    for name, grade in students.items():
        if grade >= 4:
            good_grade += f"\n{name} - {grade}; "
        elif grade <= 3:
            bad_grade += f"\n{name} - {grade}; "
    print(good_grade)
    print(bad_grade)

def main() -> None:
    students: dict[str, int] = {}
    while True:
        command = input(
            "\n1 - Add\n" \
            "2 - Show raings\n" \
            "3 - Exit from programm\n" \
            "Enter command:\n"
            ).strip()
        if command == '1':
            name, grade = add_students()
            students[name] = grade
        elif command == '2':
            sort_students(students)                           
        elif command == '3':
            print("Termination of the program.") 
            break
        else:
            print("Unknown command. Please choose 1, 2 or 3.")      

main()            

        