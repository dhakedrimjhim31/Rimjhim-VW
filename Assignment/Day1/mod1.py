def print_odd(start, end):
    i = start
    while i <= end:
        if i % 2 != 0:
            print(i)
        i += 1

def print_even(start, end):
    i = start
    while i <= end:
        if i % 2 == 0:
            print(i)
        i += 1

def print_all(start, end):
    i = start
    while i <= end:
        print(i)
        i += 1

def _base_function():
    start = int(input("Enter start number: "))
    print(type(start), start)

    end = int(input("Enter end number: "))
    print(type(end), end)

    print("1, Odd numbers")
    print("2, Even numbers")
    print("3, All numbers")

    choice = int(input("Enter your choice: "))
    print(type(choice), choice)

    if choice == 1:
        print_odd(start, end)
    elif choice == 2:
        print_even(start, end)
    elif choice == 3:
        print_all(start, end)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    _base_function()