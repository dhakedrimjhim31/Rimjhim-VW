# Take tuple elements from user
elements = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Take value to check
value = int(input("Enter value to check repetition: "))

count = elements.count(value)

if count > 1:
    print(value, "is repeated", count, "times")
elif count == 1:
    print(value, "appears only once")
else:
    print(value, "is not present in tuple")
    