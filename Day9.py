#Rock, paper, scissors.
import random
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
list_of_game = ["Rock", "Paper", "Scissors"]

if player == 0:
    print(list_of_game[0])
elif player == 1:
    print(list_of_game[1])
elif player == 2:
    print(list_of_game[2])


print("Computer chose")


random_selection_computer= random.randint (0,2)

if random_selection_computer == 0:
    print("Rock")

elif random_selection_computer == 1:
    print("Paper")

elif random_selection_computer == 2:
    print("Scissors")

#Game logic

if player == random_selection_computer:
    print("Draw")

elif player == 0 and random_selection_computer == 2: #Rock gana a tijeras
    print("You won")

elif player == 2 and random_selection_computer == 1: #Tijeras ganan a paper
    print("You won")

elif player == 1 and random_selection_computer == 0: #Paper gana contra rock
    print("You won")

else:
    print("You lose")

#Solu mas optima

# Rock, Paper, Scissors - Versión simple mejorada
import random

# Entrada del jugador
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Lista con las opciones del juego
list_of_game = ["Rock", "Paper", "Scissors"]

# Mostrar la elección del jugador usando la lista directamente
print(f"You chose: {list_of_game[player]}") #Usamos la variable player como indice
#Si player es 1 pues imprime paper
# Selección aleatoria de la computadora
random_selection_computer = random.randint(0, 2)

# Mostrar la elección de la computadora usando la lista
print(f"Computer chose: {list_of_game[random_selection_computer]}")

# Lógica del juego
if player == random_selection_computer:
    print("Draw")

elif player == 0 and random_selection_computer == 2:  # Rock gana a Scissors
    print("You won!")

elif player == 2 and random_selection_computer == 1:  # Scissors ganan a Paper
    print("You won!")

elif player == 1 and random_selection_computer == 0:  # Paper gana a Rock
    print("You won!")

else:
    print("You lose!")