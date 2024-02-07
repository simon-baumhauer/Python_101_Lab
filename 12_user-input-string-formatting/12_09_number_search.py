# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
number = input("Give me a number between 0 and 1,000,000,000")
index = 0
while int(number) != index:
    index += 1

print(f"Done {number} {index}")
