# Chris Garey #2417512
# This is original work by me, there are no other collaborators.
# Pseudocode
# Begin Prog
# prompt the user to input the temperature in celcius
# convert the temperature to fahrenheit
# print the temperature in fahrenheit back to user
# End Prog

# takes user input of current temp in celcius
celcius = float(input("Please tell me the current temperature in celcius : "))
    

# converts input to fahrenheit
fahrenheit = celcius * 9/5 + 32
    

print("The temperature in fahrenheit is : ", fahrenheit)
