# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

user_name = input("What's your name boy?")
username = ""

for index, char in enumerate(user_name):
    if char == " ":
       username = f"Hello {user_name[0:index]}"
       break
    else:
       username = f"Hello {user_name}"

print(username)
        
    
