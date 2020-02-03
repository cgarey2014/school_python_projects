# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Pseudocode
# Begin Prog
# prompt the user to input the lenth of the rectangle and store it as 'l'
# prompt the user to input the width of the rectangle and store it as 'w'
# calculate the area
# calculate the perimeter
# print the area
# print the perimeter
# End Prog

# asks for user input as to the length and width of the rectangle
l = float(input("What is the rectangle's length? : "))
w = float(input("What is the rectangle's width? : "))

# defines area and perimeter equations
area = 1 * w
perimeter = 2 * (1+w)

# prints the results
print("The area of the rectangle is:\n", format(area, '.3f'))
print("The perimeter of the rectangle is:\n", format(perimeter, '.2f'))