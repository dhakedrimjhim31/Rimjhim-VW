# Accept list from user
numbers = list(map(int, input("Enter elements separated by space: ").split()))

# Print alternate elements
print("Alternate elements are:", numbers[::2])