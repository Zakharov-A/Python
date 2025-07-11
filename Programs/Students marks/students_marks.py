import os

BASE_DIR = os.path.dirname(__file__)
FILE_NAME = 'students_grade.txt'
FILE_PATH = os.path.join(BASE_DIR, FILE_NAME)


def load_students_grade() -> dict[str, int]:
    students: dict[str, int] = {}
    if not os.path.exists(FILE_PATH):
        return students
    
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                name, grade_str = line.split(",", maxsplit=1)
                grade = int(grade_str)
            except (ValueError, IndexError):
                continue
            students[name] = grade

    print(f"Loaded {len(students)} students from {FILE_PATH}")
    return students            


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


def save_students_grade(students: dict[str, int]) -> None:
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        for name, grade in students.items():
            file.write(f"{name}, {grade}\n")
    print(f"Saved {len(students)} students to {FILE_PATH}") 


def main() -> None:
    students = load_students_grade()
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
            save_students_grade(students)
            print("Termination of the program.") 
            break
        else:
            print("Unknown command. Please choose 1, 2 or 3.")      

main()            

        