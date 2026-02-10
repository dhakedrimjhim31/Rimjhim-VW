# Accept a 4-digit number
num = int(input("Enter a 4-digit number: "))

# Extract digits
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10

# a. Face value of each digit 
print("\n Face values:")
print(thousands, hundreds, tens, ones)

# b. Place value of each digit
print("\nPlace values:")
print("Thousands place:", thousands * 1000)
print("Hundreds place:", hundreds * 100)
print("Tens place:", tens * 10)
print("Ones place:", ones * 1)

# c. Reverse the number
reverse_num = (ones * 1000) + (tens * 100) + (hundreds * 10) + (thousands * 1)

print("\n Reversed number:", reverse_num)
