# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Begin Prog
# Set the initial answer counter to zero
# Ask the first question, count one point if correct and no points if wrong.
# Ask the second question, count one point if correct and no points if wrong.
# Ask the third question, count one point if correct and no points if wrong.
# Calculate the total points

# Sets answer counter to zero
correct_answers = 0

#Starts the quiz with the first question
ounces = int(input('How many ounces are in 1 measuring cup? '))

if ounces == 8:
    correct_answers += 1
    print('Correct. Good job!')

else:
    print('Sorry, the answer is 8')

# Asks the second question
flower = input('What is the state flower of Texas? ').lower()

if flower == "bluebonnet":
    correct_answers += 1
    print('Awesome! Well done.')

else:
    print('Sorry, the answer is Bluebonnet.')

# Asks the third question
points = float(input('How many points does a octagon have? '))

if points == 8:
    correct_answers += 1
    print('Nice! That is correct.')

else:
    print('Sorry, the answer is 8')
    
print("Good job. Your final score was: ", correct_answers)