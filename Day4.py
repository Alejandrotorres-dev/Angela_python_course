print("Welcome to Treasure Island. Your mission is to find the treasure")

direction = input("Pick a direction: left or right? ").lower()

if direction == "right": 
    print("Game Over!")

elif direction == "left":
    swim_or_wait = input("Swim or wait for the boat that goes to an island ").lower()
    if swim_or_wait == "swim":
        print("Game over")
    elif swim_or_wait == "wait":
        which_door = input("Choose a door: Red, Blue or Yellow ").lower()
        if which_door == "yellow":
            print("You Win")
        else:
            print("Game Over!")