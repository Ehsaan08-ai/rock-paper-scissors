import random

options = ["rock", "paper", "scissors"]
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice(rock, paper, scissors): ")

    print(f"Players choice: {player}")
    print(f"Computers choice: {computer}")

    if player == computer:
        print("It's a Draw!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    else:
        print("You Lose!")
    
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")