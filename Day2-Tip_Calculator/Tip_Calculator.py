# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇
########## Example ##################
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Welcome Message
print("Welcome to the tip calculator!")

total_bill = input("What was the total bill?")
total_tip = input("How much tip would you like to give?")
total_people = input("How many people to split the bill?")


def calulate_tip(bill, tip, people):
    float_bill = float(bill)
    float_tip = float(tip)
    float_people = int(people)

    tip = (float_bill * float_tip) / 100
    return round((float_bill + tip) / float_people,2)


answer = calulate_tip(total_bill, total_tip, total_people)
print(answer)
