
def calc(numbers: list[str]) -> int:
    i: int = 0
    for number in numbers:
        i += int(number)
    return i 

def test() -> None:
    print('Hi bro!')   




def main() -> None:
    numbers: str = input('Enter numbers separated by commas: ')
    list_numbers: list[str] = numbers.split(', ')
    result: int = calc(list_numbers)
    print(result) 

    my_test = test()
    print(my_test)   

if __name__ == '__main__':
    main()    