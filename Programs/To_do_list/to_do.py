
def load_tasks(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tasks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(file_path: str, tasks: list[str]) -> None:
    with open(file_path, 'w', encoding='utf-8') as file :
        for task in tasks:
            file.write(task + "\n")


def main() -> None:
    FILENAME = "tasks.txt"
    to_do: list[str] = load_tasks(FILENAME)
    while True:
        print(
        "\nEnter what you want to do:\n"
        " 1 - add;\n"
        " 2 - list tasks;\n"
        " 3 - delete task;\n"
        " 4 - exit program;\n"
        )
        answer_user: str = input("Your choice: ")

        if answer_user == '1':
            task: str = input("What are we going to do? ")
            to_do.append(task)
            save_tasks(FILENAME, to_do)
            print(f"Task '{task} added'")
        elif answer_user == '2':
            if to_do:
                print("\nList of tasks: ")
                for i, task in enumerate(to_do, start=1):
                    print(f"{i}. {task}")
            else:
                print("List of tasks is empty.")    
        elif answer_user == '3':
            if to_do:
                print("List of tasks:")
                for i, task in enumerate(to_do, start=1):
                    print(f"{i}. {task}")
                try:
                    index: int = int(input("Enter the task number to delete: ")) - 1
                    if 0 <= index < len(to_do):
                        removed_task: str = to_do.pop(index)
                        save_tasks(FILENAME, to_do)
                        print(f"Task '{removed_task}' deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Input error: you must enter a number.")
            else:
                print("The task list is empty, there is nothing to delete.")
        elif answer_user == '4':
            print("The program is complete.")
            break
        else:
            print("Incorrect selection. Try again.")



if __name__ == '__main__':
    main()    