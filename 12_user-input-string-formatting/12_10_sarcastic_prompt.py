# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
user_inptu = input("Give me your opinion")
new_text = ""

for index, char in enumerate(user_inptu):
    if index % 2 == 0:
        new_text += char.upper()
    else:
        new_text += char

print(new_text)