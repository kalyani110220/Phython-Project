# src/rps.py
import random

VALID_CHOICES = ("rock", "paper", "scissors")

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(VALID_CHOICES)

def get_player_choice():
    """
    Ask the player for a choice and validate it.
    Returns the player's choice (lowercase).
    """
    while True:
        choice = input("Choose rock, paper or scissors (or 'quit' to exit): ").strip().lower()
        if choice == "quit":
            return "quit"
        if choice in VALID_CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper or scissors.")

def determine_winner(player, computer):
    """
    Determine the winner.
    Returns "player", "computer" or "tie".
    """
    if player == computer:
        return "tie"

    # Rules: rock beats scissors, scissors beat paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if wins[player] == computer:
        return "player"
    else:
        return "computer"

def play_round():
    """Play a single round, print results and return round winner."""
    player_choice = get_player_choice()
    if player_choice == "quit":
        return "quit"
    computer_choice = get_computer_choice()

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(player_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    return winner

def play_game():
    """Main game loop: keeps score until player quits."""
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        result = play_round()
        if result == "quit":
            break
        rounds_played += 1
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score} | Rounds: {rounds_played}")
        print("-" * 40)

    print("\nThanks for playing!")
    print(f"Final Score -> You: {player_score} | Computer: {computer_score} | Rounds: {rounds_played}")

if __name__ == "__main__":
    play_game()
