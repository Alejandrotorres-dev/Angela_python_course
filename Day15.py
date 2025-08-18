#En un comienzo solo me falto Mezclar y sonvertir a atring

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
n_symbols = int(input("How many symbols would you like?\n"))

# Crear una lista para almacenar todos los caracteres
# Usamo una lista porque las string son inmutables, no se pueden mezclar con el sufle.
password_list = []

# Agregar letras aleatorias a la lista
for char in range(0, n_letters): #Char se usa para contar iteraciones
    password_list.append(random.choice(letters))#Al final de la lista se anade una letra random

# Agregar símbolos aleatorios a la lista
for char in range(0, n_symbols):
    password_list.append(random.choice(symbols))

# Agregar números aleatorios a la lista
for char in range(0, n_numbers):
    password_list.append(random.choice(numbers))

# Mezclar aleatoriamente todos los caracteres
random.shuffle(password_list)
#password_list = ["k", "3", "!", "R", "$", "7"]
# Convertir la lista mezclada en string
password = ""
for char in password_list: #En este caso char si almacena los datos, no tiene rango
    password += char
print(f"Your password is: {password}")

#Char coge uno a uno los caracteres mientras recorre la lista
# y los suma a la contrasena que ahora es una string
#/Lista: ["k", "3", "!", "R"] 
       #↓ uno por uno ↓
#char:  "k" → "3" → "!" → "R"
       #↓ se suman ↓
#password: "" → "k" → "k3" → "k3!" → "k3!R"