# Taking list input
list_input = list(map(int, input("Enter list numbers: ").split()))

#Taking tuple input
tuple_input = tuple(map(int, input("Enter tuple numbers: ").split()))

# Convert both to list and tuple to strings using map
str_list = list(map(str, list_input))
str_tuple = list(map(str, tuple_input))

print("List converted to strings:", str_list)
print("Tuple converted to strings:", str_tuple)
