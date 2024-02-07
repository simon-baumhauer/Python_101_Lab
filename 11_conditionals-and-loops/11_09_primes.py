# Print out every prime number between 1 and 1000.

for number in range(100):
    if number != 0:
        if number != 1:
            if number % 2 != 0 or number == 2:
                if number % 3 != 0 or number == 3:
                    if number % 5 != 0 or number == 5:
                        if number % 7 != 0 or number == 7:
                            print(number)
     
