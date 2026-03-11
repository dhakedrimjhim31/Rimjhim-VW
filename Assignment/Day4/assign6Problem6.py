# Take input from user 
numbers = list(map(int, input("Enter numbers: ").split()))

# Double each number using map and lambda
doubled = list(map(lambda x: x * 2, numbers))

print("Original List:", numbers)
print("Doubled List:", doubled)