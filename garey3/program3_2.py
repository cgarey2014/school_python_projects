# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Begin Prog
# Prompt user for their age
# Decide if user is old enough to vote
# If they are, proceed. If not, print "Sorry, you are not old enough to vote."
# Ask user if they are a US citizen
# If yes, print "You can legally vote."
# If no, print "Sorry, only citizens can vote."

age = int(input("Please enter your age: "))

# Condition to check voting eligibility based on age
if age<18:
     print("Sorry, you are not old enough to vote.")
    
else:
    citizen = input("Are you a US citizen? (yes/no): ").lower()

    if citizen=="yes" and age>=18:
        print("You can legally vote.")

    else:
        print("Sorry, only citizens can vote.")