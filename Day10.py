import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

list_of_options = ["Rock", "Paper", "Scissors"]

print(f"You choose {list_of_options[player]}")

random_selection_computer = random.randint (0,1)

print(f"Computer chose {list_of_options[random_selection_computer]} ")