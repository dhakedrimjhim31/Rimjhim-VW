import random 
import string

length = int(input("Enter password length(8-12 recommended): "))

# character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*"

# ensure atleast one of each
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(special)
]

#fill remaining characters randomly
all_chars = uppercase + lowercase + digits + special

for i in range(length - 4):
    password.append(random.choice(all_chars))

#shuffle password
random.shuffle(password)

# convert list to string
final_password = "".join(password)

print("Generated Password:", final_password)
