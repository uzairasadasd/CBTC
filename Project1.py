#Name: Uzair Ahmed Abdul Samad Ansari
#rock paper scissors game
import random

def tournament_style(players):
    choices = ["rock", "paper", "scissors"]
    rounds = []

    for i in range(0, len(players), 2):
        user1_choice = players[i]
        user2_choice = players[i + 1]
        user1_choice = random.choice(choices)
        user2_choice = random.choice(choices)

        print(f"{players[i]} chose: {user1_choice}")
        print(f"{players[i+1]} chose: {user2_choice}")

        if user1_choice == user2_choice:
            print("It's a tie!")
            rounds.append("tie")
        elif (user1_choice == "rock" and user2_choice == "scissors") or \
             (user1_choice == "scissors" and user2_choice == "paper") or \
             (user1_choice == "paper" and user2_choice == "rock"):
            print(f"{players[i]} wins!")
            rounds.append(players[i])
        else:
            print(f"{players[i+1]} wins!")
            rounds.append(players[i+1])

    print(f"Round winners: {rounds}")

tournament_style(["Player 1", "Player 2", "Player 3", "Player 4"])
