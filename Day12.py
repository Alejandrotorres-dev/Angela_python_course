#saca el valor max de esta lista
student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

max_score = 0

for student in student_scores:
    if student > max_score: #student es cada uno de los valores en la lista
        max_score = student

print(max_score)

#El código busca el número más grande en una lista 
# comparando cada elemento con el valor máximo encontrado hasta ese momento.