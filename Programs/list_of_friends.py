def main() -> None:
    # Option 1

    # def my_list() -> None: 
    #     names: list = ["Ivan", "Maria", "Petr", "Andrey", "Lena"]
    #     friend_name: str = input("Enter name for chek: ")
    #     for name in names:
    #         if friend_name == name:
    #             print(f"Name {friend_name} found")

    #     if friend_name not in names:
    #         print(f"Name {friend_name} not found")

    # my_list()

    # Option 2            

    def search_name() -> None: 
        list_names = ["Ivan", "Maria", "Petr", "Andrey", "Lena"]
        name = input("Enter name for chek: ")
        name = name.title()
        if name in list_names:
            print(f"Name {name} found")
        else:
            print(f"Name {name} not found")

    search_name()    
    

if __name__=="__main__":
    main()     