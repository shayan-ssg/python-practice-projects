import random

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))

    attempts += 1

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Correct!")
        print(f"You won in {attempts} attempts.")
        break