import random

options = ["rock", "paper", "scissors"]
running = True

wins = 0
losses = 0
ties = 0

while running:
    print('%s Wins, %s Losses, %s Ties'%(wins, losses, ties))
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice(rock, paper, scissors): ")

    print(f"Players choice: {player}")
    print(f"Computers choice: {computer}")

    if player == computer:
        print("It's a Draw!")
        ties += 1
    elif player == "rock" and computer == "scissors":
        print("You Win!")
        wins += 1
    elif player == "scissors" and computer == "paper":
        print("You Win!")
        wins += 1
    elif player == "paper" and computer == "rock":
        print("You Win!")
        wins += 1
    else:
        print("You Lose!")
        losses += 1
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")