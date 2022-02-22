"""

Software for calculate who's are the higher number
Author: Leonardo Miguel
Date: 12/02/2022
Description:
    This software has the proposal to calculate
three values and show for user what's the number is higher.
"""

# Declarations
value_one = int(input("Type the first number: "))
value_two = int(input("Type the second number: "))
value_three = int(input("Type the third number: "))


plus = value_one
if value_two > value_one and value_two > value_three:
    plus = value_two
elif value_three > value_one and value_three > value_two:
    plus = value_three
    print("The highest number: {}".format(plus))
    input("Press enter to shutdown...")
else:
    print("Not a equal number. Because we are trying to find the higher number")
    input("Press enter to shutdown...")
# End of the software
