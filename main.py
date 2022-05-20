# Project 3
# Treasure Island

from art import treasure_box, diamond

# greet user
print(treasure_box)
print("Welcome to Treasure Island.")

# get input left or right
turn = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n")

if turn.lower() == "left":
    # get input swim or wait
    lake = input("You have arrived at a lake. Type 'wait' to wait for a boat or 'swim' to start swimming.\n")

    if lake.lower() == "wait":
        print("You have reached the treasure island.")
        # get input red, green or blue door
        door = input("There are 3 doors: green, red, blue. Type which one to open.\n")

        if door.lower() == "green":
            print("You've found the treasure. Congrats you won the game.")
            print(diamond)
        else:
            print("There were monsters behind the door. Game over.")
    else:
        print("You got attacked by sharks. Game over.")
else:
    print("You fell in a hole. Game over.")
