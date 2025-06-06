import random


def play(tips=False):
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0
    max_attempts = 10

    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
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


while True:
    if input("Do you want to play with tips? (yes/no): ").strip().lower() == "yes":
        play(True)
    else:
        play()
    if input("Play again? (yes/no): ").strip().lower() != "yes":
        print("Thanks for playing!")
        break
