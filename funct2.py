def greet_with (name, location):
    print(f"Hello {name}")
    print(f"We are in {location}")

greet_with("Alex", "Pamplona")

#Con keyword arguments en vez de position arguments:

def greet_with (name, location):
    print(f"Hello {name}")
    print(f"We are in {location}")

greet_with(location = "Pamplona", name = "Alex")


list = ["1", "2", "3"]

print(len(list))

print(list[-2])

