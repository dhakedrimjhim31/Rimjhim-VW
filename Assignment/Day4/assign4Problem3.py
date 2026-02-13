def subtract(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("Subtract:", subtract(list1, list2))