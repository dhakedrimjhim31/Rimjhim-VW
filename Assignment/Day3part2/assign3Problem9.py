dict1 = {'key 1': 200, 'key 2': 300}


total = 0

for value in dict1.values():
    total += value

print("Result:", total)

# Take input of items fro user
n = int(input("Enter number of key-value pairs: "))

dict1 = {}

# Take key-value input
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Calucate sum
total = 0
for value in dict1.values():
    total += value

print("Result:", total)