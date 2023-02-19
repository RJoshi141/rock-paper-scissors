import random

# Define the choices
choices = ["rock", "paper", "scissors"]

# Prompt the player to choose rock, paper, or scissors
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate the player's choice
while player_choice not in choices:
    player_choice = input("Invalid input. Please choose rock, paper, or scissors: ").lower()

# Randomly choose rock, paper, or scissors for the computer
computer_choice = random.choice(choices)

# Determine the winner
if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
else:
    if computer_choice == "rock":
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
