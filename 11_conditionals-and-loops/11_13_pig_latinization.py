# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay
import string

text = """You would never guess what can happen when you jump into a seemingly shallow puddle at night time!"""
neuer_text = ""
lastChar = text[0].lower()

for index, char in enumerate(text):
    if char == " ":
        neuer_text += lastChar + "ay " 
        lastChar = text[index + 1].lower()
    elif char == "!":
        neuer_text += lastChar + "ay" + "!"
    elif text[index - 1] == " " or index == 0:
        pass
    else:
        neuer_text += char
print(neuer_text)



