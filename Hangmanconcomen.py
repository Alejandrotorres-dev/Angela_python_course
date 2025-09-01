import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
lives = 6
#1- Randomly choose a word from the word_list and assign it to a varriable called chosen_Word.THen print it.
#2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#3 - Check if the letter the user guessed(guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if its not.

chosen_word = random.choice(word_list)
print(chosen_word)

#guess = input("Guess a letter: ").lower()

#for i in chosen_word:
    #if i == guess:
        #print ("Right") 
    #else:
        #print("Wrong")
#print(chosen_word)

#4 If the words has 6 characteres or letters 6 _ should be printed out
placeholder = ""
word_length = len(chosen_word)
for i in range (word_length):
    placeholder += "_"
print (placeholder)

# Create a display that puts the guess letter in the right positions and _ 

#display = ""

#for letter in chosen_word:
    #if letter == guess:
        #display += letter
    #else:
        #display += "_"

#print(display)

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters
#in the chosen_word. 
#At that point display has no more blaanks("_"). Then you can tell the user they have won.

game_over = False
correct_letters = []

while not game_over: #not false es True, como el resultado es True el bucle continua.
    guess = input("Guess a letter: ").lower()

#"Mientras el juego NO haya terminado, sigue ejecutando este código"
#El bucle se detendria solo si en algun momento game over cambia a True

#Update the for loop so that previous guesses are added to the display string
#At the moment, when the user makes a new guess, the previous guess gets replaces by
# a "_". We need to fix that by updating the for loop

    display = ""

    for letter in chosen_word:
        if letter == guess: ##La b, Si la letra actual coincide con lo que adivinaste
            display += letter #Se añade al display
            correct_letters.append(letter) #La b se añade tbn a la lista

        elif letter in correct_letters: #Letras ya adivinadas visibles
            display += letter # La b ya esta en lista correctletters esa letra tambien se añade al display
            # para mantenerla en el siguiente intento en el que hemos puesto n
        else:
            display += "_" #Si no la has adivinado, muestra guión bajo

    print(display)

    if "_" not in display: # at this point the guessed everything.
        game_over = True #El while loop se detiene.
        print("You win. ")


['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']