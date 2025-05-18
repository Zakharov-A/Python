def main() -> None:
    list_numbers: tuple[int, int, list[int], int, int] = (1, 2, [22, 33], 4, 5)
    print(list_numbers)

    list_numbers[2][0] = 56

    print(list_numbers)
   

main() 