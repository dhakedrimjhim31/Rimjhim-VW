marks = {}

for i in range(3):
    subject = input("Enter subject name: ")
    score = int(input("Enter marks: "))
    marks[subject] = score

print("Marks dictionary:", marks)