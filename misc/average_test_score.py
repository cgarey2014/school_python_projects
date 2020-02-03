# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Begin Prog
# Prompt user for first test score
# Prompt user for second test score
# Prompt user for third test score
# Divide total of test scores entered by "3"
# Print the average of the three test scores, accurate to two decimal places, with the symbol "%" following immediately after the final digit.

test1 = int(input("Please enter the first test score. "))
test2 = int(input("Please enter the second test score. "))
test3 = int(input("Please enter the third test score. "))

total = test1 + test2 + test3
avg = total / 3.0
print("Average is: ", format(avg, ',.2f'), "%", sep='')