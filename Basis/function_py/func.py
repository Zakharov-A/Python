
# def main():
#     for i in "Hello Django School":
#         print(i)

# if __name__ == "__main__":
#     main()

# def main():
#     name = "Jora".upper()
#     n = 0
#     for i in name:
#         n += 1
#         print(n, i)

# if __name__ == "__main__":
#     main()

def main():
    name = "Jora".upper()
    for n, i in enumerate(name):
        print(n, i)

if __name__ == "__main__":
    main()