import json 
import os

def load_contacts(filename: str) -> dict:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Ошибка чтения файла. Загружаем пустой список контактов")
                return {}
    return{}


def save_contacts(contacts: dict, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

def main() -> None:
    filename = 'contacts.json'

    contacts: dict[str, dict[str, int | str]] = load_contacts(filename)
        
    while True:
        command: str = input(""
        "\n1 - Добавить\n"
        "2 - Удалить\n"
        "3 - Просмотр\n"
        "4 - Изменить\n"
        "5 - Выход из программы\n"
        "\nВведите команду: ")
        print()
        if command == '1':
            name: str = input("Введите имя: ")
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            try:
                tel: int = int(input("Введите телефон: "))
            except ValueError:
                print("Неверный формат номера телефона.") 
                continue   
            email: str = str(input("Введите электронную почту: "))

            contacts[name] = {'phone': tel, 'email': email}
            print(f"\nДобавлен новый контакт:\nИмя - {name}. Телефон - {tel}. Почта - {email}.")
            save_contacts(contacts, filename)

        elif command == '2':
            name: str = input("Введите имя: ")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Контакт {name} удален.")
            else:
                print(f"Имя {name} не найдено")
        elif command == '3':
            if contacts:
                for name, info in contacts.items():
                    print(f"{name} - {info['phone']} - {info['email']}")
            else:
                print("Список контактов пуст.")    

        elif command == '4':
            name = input("Введите имя контакта: ")
            if contacts.get(name):
                try:
                    tel: int = int(input("Введите номер телефона: "))
                except ValueError:
                    print("Неверный формат номера телефона.")    
                email: str = input("Введите электронную почту: ")
                contacts[name] = {'phone': tel, 'email': email}
                print(f"\nИзменен контакт:\nИмя - {name}. Телефон - {tel}. Почта - {email}.")
                save_contacts(contacts, filename)

            else:
                print(f"Имя {name} не найдено")
                
        elif command == '5':
            print("Завершение работы программы.")
            break                              

if __name__ == "__main__":
    main()          