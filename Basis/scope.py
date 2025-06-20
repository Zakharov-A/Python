name: str = 'Mike'

def func() -> None:
    name: str = 'John'
    print(f"Var name in func = {name}")

func()    

def func_2():
    global name_2
    name_2 = 'Lena'
    print(f"Var name_2 in func_2 = {name_2}")

func_2()    


def func_3():
    # name_2 = 'Bob'
    print(f"Var name_2 in func_3 = {name_2}")

func_3()       