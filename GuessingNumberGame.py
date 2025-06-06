import random


def play(tips=False):
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 10

    while True:
        try:
            attempts += 1
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10.")
                continue
            if guess == secret_number:
                print(f"You guessed it in {attempts} tries!")
                return
            elif attempts == max_attempts:
                print(f"You lost! Correct number: {secret_number}!")
                return
            else:
                print("Try again!")
            if tips:
                if guess > secret_number:
                    print("Secret number is lower")
                else:
                    print("Secret number is bigger")
        except ValueError:
            print("Enter a number please!")


def is_yes(text):
    return text.strip().lower() in {"yes", "y"}


while True:
    if is_yes(input("Do you want to play with tips? (yes/no): ")):
        play(True)
    else:
        play()
    if not is_yes(input("Play again? (yes/no): ")):
        print("Thanks for playing!")
        break
