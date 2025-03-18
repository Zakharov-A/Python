def main():
    contacts = {"Petr": 111222, "Lena": 443322, "Andre": 556677}
    print(contacts)
    contacts["Petr"] = "112233"
    print(contacts)
    contacts["John"] = 100000
    print(contacts)
    print(contacts.get("Dasha", "Error"))

main()    