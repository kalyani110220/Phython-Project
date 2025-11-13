import random

def play_game():
    min_val, max_val = 1, 100
    secret = random.randint(min_val, max_val)
    attempts = 0

    print(f"Guess the number between {min_val} and {max_val}!")

    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print("Please enter a valid integer.")
            continue
        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
