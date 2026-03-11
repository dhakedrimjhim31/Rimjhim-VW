def histogram(numbers):
    for num in numbers:
        print("*" * num)

# Example 
#histogram([4,9,7])

# Take input from user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Call function
histogram(numbers)