import math

def circle():
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    perimeter = 2 * math.pi * r
    print("Area:", area)
    print("Perimeter:", perimeter)

def square():
    s = float(input("Enter side: "))
    area = s * s
    perimeter = 4 * s
    print("Area:", area)
    print("Perimeter:", perimeter)

def rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    perimeter = 2 * (l + b)
    print("Area:", area)
    print("Perimeter:", perimeter)

print("1. Circle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter choice: "))

if choice == 1:
    circle()
if choice == 2:
    square()
if choice == 3:
    rectangle()
else:
    print("Invalid choice")