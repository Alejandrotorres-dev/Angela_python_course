import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
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

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over: #while not False = while True, el bucle funciona
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word: #Recorre cada letra de la palabra, todas las letras por turno.
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters: #Letra x ya adivinada la muestra
            display += letter
        else:
            display += "_"

    print(display) #Imprimir una vez por intento, tras el for procesado all letters.

    if "_" not in display:
        game_over = True #While not true = while False, bucle para.
        print("You win.")
    
    if guess not in chosen_word:
        lives -= 1
    
        if lives == 0: # Si ya no quedan vidas
            game_over = True
            print("You lose.")

    print(stages[lives]) #Lo queremos mostrar en cada turno.

#Tanto el for como los if están dentro de while porque se ejecutan
#por cada intento, pero el for por cada letras y cada uno de los if
#solo una vez tras el for.
#el if anidado tiene sentido porque solo se llega a 0 tras el jugador pierde 1 vida mas de 1 a 0