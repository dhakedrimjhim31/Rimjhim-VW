import random 

secret_number = random.randint(1, 100)
attempts = 7

print("Guess the numberbetween 1 and 100")
print("You have 7 attempts")

for i in range(attempts):

    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try a smaller number.")
    elif guess < secret_number:
        print("Too low! Try a lager number.")
    else:
        print("Congratulations! You guessed correctly!")
        break
    
else:
    print("Sorry! You lost.")
    print("The correct number was:", secret_number)