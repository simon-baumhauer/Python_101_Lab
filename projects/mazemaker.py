# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

word = "schwein"
blanks = ""
user_input = ""
lifes = 0
user_guess = ""
print_state = ""


print("You have to guess the word, lets go!!")
for char in word:
    blanks += " _ "
print(f"This is the word {blanks}")

while len(word) != len(user_guess) and lifes < 4:
    user_input = input("Add a character \n")
    if not isinstance(user_input, str) or len(user_input) != 1:
        print(f"{isinstance(user_input, str)}{len(user_input) != 1}")
        continue
    else:
        for index, char in enumerate(word):
            if char == user_input:
                lifes = 0
                print_state = ""
                for char in word:
                    if user_input == char:
                        print_state += f" {char} "
                        user_guess += char
                    else:
                        print_state += " _ "
                print(F"{print_state}")
    continue

if len(user_guess) == len(word): 
    print("You win")
else:
    print(f"You lost {len(word)} {len(user_guess)} {lifes}")