# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
user_input = input("Tell me something?")
new_text = ""
for index, char in enumerate(user_input):
        if char == user_input[0]:
            new_text += "§"
        else:
            new_text += char
    
print(new_text)
