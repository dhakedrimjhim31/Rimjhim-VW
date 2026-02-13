numbers = []

print("Enter 6 numbers:")
for i in range(6):
    num = int(input())
    numbers.append(num)

result = {'EVEN': [], 'ODD': []}

for num in numbers:
    if num % 2 == 0:
        result['EVEN'].append(num)
    else:
        result['ODD'].append(num)

print(result)