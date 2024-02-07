# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

for number in range(1000):
    if number % 5 == 0:
        print(number)
