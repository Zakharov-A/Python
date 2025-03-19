def main() -> None:
    contacts: dict[str, int] =  {"Petr": 111222, "Lena": 443322, "Andre": 556677}
    while True:
        command: str = input(""
        "\n1 - Добавить\n"
        "2 - Удалить\n"
        "3 - Просмотр\n"
        "4 - Выход из программы\n"
        "\nВведите команду: ")
        print()
        if command == '1':
            name: str = input("Введите имя: ")
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            tel: int = int(input("Введите телефон: "))
            contacts[name] = tel
        elif command == '2':
            name: str = input("Введите имя: ")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Контакт {name} удален.")
            else:
                print(f"Имя {name} не найдено")
        elif command == '3':
            for name, phone in contacts.items():
                print(f"{name} - {phone}")            


main()    