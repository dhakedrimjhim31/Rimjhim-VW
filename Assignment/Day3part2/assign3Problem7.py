# Take input from user
#num = [2, 3, 4, 5, 2, 6, 3, 2]
num = list(map(int, input("Enter numbers separated by space: ").split()))

new_list = []

for item in num:
    if item not in new_list:
        new_list.append(item)

print("Result:", new_list)