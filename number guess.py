import random 

number = random.randint(1, 50)

print("Guess the number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print(" low! Try again.")
    elif guess > number:
        print(" high! Try again.")
    else:
        print("Correct! You win ")
        break
