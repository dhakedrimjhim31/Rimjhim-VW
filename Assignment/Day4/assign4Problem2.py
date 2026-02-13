def union(list1, list2):
    result = list1.copy()
    for item in list2:
        if item not in result:
            result.append(item)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("Union:", union(list1, list2))