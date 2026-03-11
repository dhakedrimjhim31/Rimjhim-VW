import random
import string

captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print("CAPTCHA:", captcha)

user_input = input("Retype the CAPTCHA exactly: ")

if user_input == captcha:
    print("Verfication Successful!")
else:
    print("Incorrect CAPTCHA. Try again.")