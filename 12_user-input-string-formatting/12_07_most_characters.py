# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string_one = input("Give me a string")
string_two = input("Give me a string")
string_tree = input("Give me a string")

if len(string_one) > len(string_two) and len(string_one) > len(string_tree):
    print(string_one)
elif len(string_two) > len(string_two) and len(string_two) > len(string_tree):
    print(string_two)
else:
    print(string_tree)


