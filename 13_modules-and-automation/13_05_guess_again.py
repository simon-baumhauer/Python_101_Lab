# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
random_number = random.randrange(1,10)
user_input = 0
lifes = 3

while random_number != user_input:
    user_input = int(input("Give me a number between one and ten"))
    if random_number == user_input:
        print(f"you got it!")
        break
    else:
        print(f"you were wrong")
        lifes -= 1
        if lifes == 0:
            print("No life left :(")
            break
