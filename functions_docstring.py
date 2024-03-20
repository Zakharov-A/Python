# # Example 1

# def mult_by_factor(value, mult=1):
#     """Multiplies number by multiplicator"""
#     return value * mult


# print(mult_by_factor(5))

# # Example 2

def print_number_info(num):
    """
    Prints num information

    Args:
        num (int): Integer number

    Returns:
        int: Same number
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")

    return num

print_number_info(21)


