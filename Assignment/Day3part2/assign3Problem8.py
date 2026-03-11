people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'purple', 'Jenny': 'Pink'}

# A. Count students
print("Number of students:", len(people))

# B. Change Lisa's favourite colour
people['Lisa'] = 'Green'

# C. Remove Jenny
people.pop('Jenny')

# D. sort and print alphabetically
for name in sorted(people):
    print(name, ":", people[name])