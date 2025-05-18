def main() -> None:
    contacts: dict[str, dict[str, int | str]] = {
        "Petr": {'Phone': 111222, 'Email': "petr@kaka.ru"},
        "Lena": {'Phone': 443322, 'Email': 'lena@kaka.com'}, 
        "Andre":{'Phone': 556677, 'Email': 'andrey@kaka.org'},
        }
    
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")

    print()
    contacts['Petr']['Phone'] = 666555
    contacts['Petr']['Email'] = 'kind@bigboss.ru'
    
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    
    
    
if __name__ == "__main__":
    main()          