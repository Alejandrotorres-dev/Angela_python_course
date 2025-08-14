import random

#random_integer = random.randint(1,10) #Números enteros aleatorios en un rango (inclusive)
#print(random_integer)
# la funcion randint toma como input el rango 1,10

#random_number_0_to_1 = random.random() #Número decimal entre 0.0 y 1.0 (no incluye 1.0) 
#print(random_number_0_to_1)#se usa para probabilidades

#random_float = random.uniform(1,10) # Número decimal en un rango específico
#print(random_float)

random_coin = random.randint (0,1)

if random_coin == 0:
    print("Head")
else:
    print("Tails")