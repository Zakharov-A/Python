from typing import Dict, Union

def main() -> None:
    contacts: Dict[str, Dict[str, Union[int, str]]] = {
        "Petr": {'Phone': 111222, 'Email': 'petr@kaka.ru', 'home_address': 'Vishnevay 17'},
        'Lena': {'Phone': 443322, 'Email': 'lena@kaka.ru', 'home_address': "Lipovay 11"},
        'Andre': {'Phone': 556677, 'Email': 'andrey@kaka.org', 'home_address': "Budenova 28"},
    }

    print()

    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info.get('Phone', 'not specified')}, Email: {info['Email']}, Home address: {info['home_address']}, Second address: {info.get('second_address', 'not specified')}")

    print()

    contacts['Petr']['Phone'] = 666555
    contacts['Petr']['Email'] = 'big_boss@jopa.org'
    contacts['Petr']["home_address"] = "Novorublevo 1"

    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info.get('Phone', 'not specified')}, Email: {info['Email']}, Home address: {info['home_address']}")    

if __name__ == "__main__":
    main()       