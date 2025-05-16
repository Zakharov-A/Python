def main():
    contacts = {
        "Petr": {'Phone': 111222, 'Email': "petr@kaka.ru"},
        "Lena": [443322, 'lena@kaka.com'], 
        "Andre": [556677, 'andrey@kaka.org'],}
    print(contacts)
    contacts["Petr"][0] = 666555
    contacts['Petr'][1] = 'kind@bigboss.ru'
    contacts['John'] = {'Phone': 666999, 'Email': "john@kaka.ru"}
    print(contacts)
    print(contacts['Lena'][0], contacts['Lena'][1])
    print(f"Phone: {contacts['Petr']['Phone']}, Email: {contacts['Petr']['Email']}")
    
    

main()    