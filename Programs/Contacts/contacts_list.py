def main() -> None:
    contacts: dict[str, int] =  {"Petr": 111222, "Lena": 443322, "Andre": 556677}
    while True:
        command: str = input(""
        "1 - Добавить\n"
        "2 - Удалить\n"
        "3 - Просмотр\n"
        "4 - Выход из программы\n")
        if command == '1':
            name: str =input("Введите имя: ")
            tel: int = int(input("Введите телефон: "))
            contacts[name] = tel
        print(contacts)    



main()    