# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Begin Prog
# Prompt user to enter cost of meal, then ask if tip will be added.
# If tip is added, prompt for tip percentage as integer
# Print the total cost of meal
# Print the total tip amount
# Print the total bill amount

cost = float(input("What is the cost of the meal? "))
answer = input("Will a tip be added to the bill? (yes/no) ").lower()
# Asks the user if a tip is being added to the cost, if not, then prints cost without tip.
if answer == "yes":
        tip = float(input("Enter the tip percent as an integer: "))
        tip = cost * tip
        total = cost + tip
        print("The cost of the meal is: $", format(cost, ',.2f'), sep='')
        print("The total tip amount is: $", format(tip, ',.2f'), sep='')
        print("The total cost is: $", format(total, ',.2f',), sep='')
elif answer == "no":
        tip = 0
        total = cost
        print("The cost of the meal is: $", format(cost, ',.2f'), sep='')
        print("The total tip amount is: $", format(tip, ',.2f'), sep='')
        print("The total cost is: $", format(total, ',.2f',), sep='')