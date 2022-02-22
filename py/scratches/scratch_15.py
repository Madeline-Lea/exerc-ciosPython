"""
Oh, Positive or Negative Software
Author: Leonardo Miguel
Date: 13/02/2022
Description:
    The software has one objective as type a number
and see if this number is equal a 0, Positive or Negative.
Tools: Pycharm & w3Schools
"""

# Declarations

# This line grab the number it was typed
verify_number = int(input("Type a number to be verified: "))

# Conditionals

# This line validate if the number is negative

if verify_number < -1:
    print("This number is negative")
    input("Press enter to shutdown")

# This line validate if the number is equal an Oh

elif verify_number == 0:
    print("This number is equal a Oh")
    input("Press enter to shutdown")

# This line validate if the number is positive

elif verify_number > 1:
    print("This number is positive")
    input("Press enter to shutdown")
else:
    print("Type a valid number.")
