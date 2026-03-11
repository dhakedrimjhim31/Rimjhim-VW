def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Take input from user
list1 = list(map(int, input("Enter elements of first line separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

# Call function
result = overlapping(list1, list2)

print("Do the lists have atleast one common element?", result)