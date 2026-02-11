# Take input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Assume first number is largest
largest = numbers[0]

# Compare with remaining elements
for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

        