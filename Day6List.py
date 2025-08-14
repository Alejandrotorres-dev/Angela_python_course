states_of_america = ["Delaware", "Pennsylvania"]
#Store many pieces of related data, and the orden is important too.

#print(states_of_america[1])
# Puedo alterar un item de la lista asi:
states_of_america[1] = "Pencilvania"
#print(states_of_america)
# o add alguien al final con la func append, add a single item
states_of_america.append("Alexland")
print(states_of_america)

states_of_america.extend #permite add varios items at the end of the list.
states_of_america.extend(["Angeland","Jackland"])