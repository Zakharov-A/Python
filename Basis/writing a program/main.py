def main() -> None:
    students = {}
    while True:
        command = input("1 - Add\n2 - View\n3 - Enter command\n4 - Exit the progam\n")
        if command == '1':
            name = input("Enter name: ")
            grade = input("Enter rating: ")
            students[name] = grade
            print(students)
        if command == '4':
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


