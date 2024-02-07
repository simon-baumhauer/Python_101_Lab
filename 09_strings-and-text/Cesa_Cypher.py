lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


import string



for char in secret:
    if char != " " and char not in string.punctuation:
        crypto_test += char
        for index, letter in enumerate(alphabet):
            if letter == char:
                print(index)




