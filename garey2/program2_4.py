# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Pseudocode
# Begin Prog
# store value of $1.00 to a variable called dollar
# prompt the price in cents and store to a variable called cents
# print the change due
# print the amount of quarters
# print the amount of dimes
# print the amount of nickels
# print the amount of pennies
# End Prog

# asks for the user to input price of the item
price = int(input('Enter the price of the item in cents : '))

# calculates change due from $1.00
rest = (100 - price)

# prints the change due
print ('Change due is', rest, 'cents. Returning as: ')

#Defines calculations for each denomination
quarters = (rest // 25)
rest = (rest - 25 * quarters)
dimes = (rest // 10)
rest = (rest - 10 * dimes)
nickles = (rest // 5)
rest = (rest - 5 * nickles)
pennies = rest
    
print ("Quarters: ", quarters)

print ("Dimes: ", dimes)

print ("Nickles: ", nickles)

print ("Pennies: ", pennies)