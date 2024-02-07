# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
amount = input("How much money do you want to invest?")
percent = input("How high is the intrest rate?")
years = input("how many year you want to keep it invested?")
profit = 0

for year in years:
    profit = (float(amount) * float(percent)) 

print(str(profit))