def main() -> None:
    to_do: list[str] = []
    while True:
        print(
        "Enter what you want to do:\n"
        " 1 - add;\n"
        " 2 - list tasks;\n"
        " 3 - delete task;\n"
        " 4 - exit program;\n"
        )
        answer_user: str = input("Your choice: ")

        if answer_user == '1':
            task: str = input("What will we do? ")
            to_do.append(task)
            print(f"Task '{task} added'")
        elif answer_user == '2':
            if to_do:
                print("List of tasks: ")
                for i, task in enumerate(to_do, start=1):
                    print(f"{i}. {task}")
            else:
                print("List of tasks is empty.")    
        elif answer_user == '3':
            if to_do:
                print("Список задач:")
                for i, task in enumerate(to_do, start=1):
                    print(f"{i}. {task}")
                try:
                    index: int = int(input("Введите номер задачи для удаления: ")) - 1
                    if 0 <= index < len(to_do):
                        removed_task: str = to_do.pop(index)
                        print(f"Задача '{removed_task}' удалена.")
                    else:
                        print("Некорректный номер задачи.")
                except ValueError:
                    print("Ошибка ввода: нужно ввести число.")
            else:
                print("Список задач пуст, нечего удалять.")
        elif answer_user == '4':
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")



if __name__ == '__main__':
    main()    