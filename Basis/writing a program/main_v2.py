def add_students() -> tuple[str, int]:
    name: str = input("Enter name: ")
    while True:
        try:    
            grade: int = int(input("Enter rating: "))
        except ValueError:
            print("You have not entered a number. Enter a number!") 
            continue 
        else:
            return name, grade


def sort_students(students) -> None:
    good_grade: str = "Entered: "
    bad_grade: str = "Didn't enter: "
    for name, grade in students.items():
        if grade >= 4:
            good_grade += f'\n{name} - {grade}'
        elif grade <= 3:
            bad_grade += f'\n{name} - {grade}'
    print(good_grade)            
    print(bad_grade)  

def main() -> None:
    students: dict[str, int] = {}
    while True:
        command: str = input("1 - Add\n2 - View\n3 - Enter command\n4 - Exit the progam\n")
        if command == '1':
            name, grade = add_students()
            students[name] = grade
        elif command == '2':
             sort_students(students)         
        elif command == '4':
            print("The program has completed its work.")
            break    

if __name__ == '__main__':
    main()            







"""
Поступили:
имя - оценка
================
Не поступили:
имя - оценка
================
['name - value', 'name - value']
"""


