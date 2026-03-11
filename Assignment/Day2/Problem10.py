# Take marks input from user
mark1 = int(input("Enter marks of subject 1: "))
mark2 = int(input("Enter marks of subject 2: "))
mark3 = int(input("Enter marks of subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine grade
if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
else:
    grade = "F"

# Display result
print("Average Marks:", average)
print("Grade:", grade)