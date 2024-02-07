# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

name = input("What is your Name?")
sword = False
status = False
print(f" Hello {name} this is a game to play")
while status == False:
     firstChoice = input("Do you go left or right?")
     if firstChoice == "left":
        secondChoice = input("'ll see an empty room. Do you want to return or look around")
        if secondChoice == "look around":
            thirdChoice = input("You found a sword you to take it yes or no?")
            if thirdChoice == "yes":
                print("you wil go back now")
                sword = True
                continue
     elif firstChoice == "right":
        print("There is a Dragon")
        secondChoice = input("Do you want to return or fight?")
        if secondChoice == "fight":
            if sword == True:
                print("Win!!!")
                status = "Win!!!"
                break
            else:
                print("Lose!!")

   
