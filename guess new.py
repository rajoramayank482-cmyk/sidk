import random 

number = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    if guess>100 or guess< 1:
        print("invalid!")
    if guess < number:
        print(" low! Try again.")
    elif guess > number:
        print(" high! Try again.")
    else:
        print("Correct! You win ")
        break
