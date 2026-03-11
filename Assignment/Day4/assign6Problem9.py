def even_position(text):
    print("Even position characters:", text[1::2])

def odd_position(text):
    print("Odd position characters:", text[0::2])

def length_string(text):
    print("Length of string:", len(text))

def add_a(text):
    result = text + "a" * len(text)
    print("Result:", result)

text = input("Enter a string: ")

print("A. Even position")
print("B. Odd position")
print("C. Length")
print("D. Add 'a' length times")

choice = input("Enter choice: ")

if choice == 'A':
    even_position(text)
elif choice == 'B':
    odd_position(text)
elif choice == 'C':
    length_string(text)
elif choice == 'D':
    add_a(text)
else:
    print("Invalid choice")