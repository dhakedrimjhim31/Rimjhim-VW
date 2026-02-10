def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
     
# Call function
result = max_of_three(num1, num2, num3)

# Display result
print("Maximum number is :", result)
