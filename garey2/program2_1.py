# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Pseudocode
# Begin Prog
# prompt the user to input hours worked and store it as a variable called hours
# prompt the user to input hourly pay rate and store it as a variable called payRate
# calculate gross pay as hours worked by multiplied pay rate
# print the gross pay
# End Prog

# asks for user input for the amount of hours and payrate
hours = float(input("Please enter your hours worked this week:\n"))
payRate = float(input("Please enter your hourly rate of pay\n"))

#calculates the weekly pay
weeklyPay = hours * payRate

# prints the results of the calculations
print("Your weekly pay is\n$", format(weeklyPay, ',.2f',) ,sep='')
