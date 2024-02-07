# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

number = 0

while number not in range(1, 13):
    user_input = input("Give me number between 1 - 12")
    number = int(user_input)
    if number == 1:
        print("january")
    if number == 2:
        print("feburary")
    if number == 3:
        print("march")
    if number == 4:
        print("april")
    if number == 5:
        print("may")
    if number == 6:
        print("june")
    if number == 7:
        print("july")
    if number == 8:
        print("august")
    if number == 9:
        print("september")
    if number == 10:
        print("october")
    if number == 11:
        print("nomber")
    if number == 12:
        print("december")
print("break")
